import cv2
import nibabel as nib
import numpy as np
from tqdm import tqdm
from ultralytics import YOLO

from .utils import download_model


def predict(data, axis, verbose):
    """
    Generate a binary tumor mask from a 3D image array using a trained YOLO model.
    Args:
        data (np.ndarray): 3D image array (e.g., FLAIR image).
        axis (int): Axis along which to slice the 3D image (0: sagittal, 1: coronal, 2: axial).
        model (YOLO): Loaded YOLO model.
        verbose (bool): Whether to print statistics.
    Returns:
        np.ndarray: Binary mask of detected tumor regions.
    """

    assert axis in [0, 1, 2], "Axis must be 0 (sagittal), 1 (coronal), or 2 (axial)."

    # Load the YOLO model
    model_path = download_model(axis, verbose)
    model = YOLO(model_path)

    # Initialize binary mask with same shape as input
    binary_mask = np.zeros_like(data, dtype=np.uint8)
    n_slices = data.shape[axis]  # Number of coronal slices

    # Process each coronal slice
    for i in tqdm(range(n_slices), desc="Detecting tumors", disable=not verbose):
        # Extract slice
        if axis == 0:
            slice_data = data[i, :, :]
        elif axis == 1:
            slice_data = data[:, i, :]
        else:
            slice_data = data[:, :, i]

        # Normalize slice to 0-255 for YOLO input
        slice_min, slice_max = np.min(slice_data), np.max(slice_data)

        if slice_max - slice_min == 0:
            continue  # Skip empty slices

        normalized_slice = ((slice_data - slice_min) / (slice_max - slice_min) * 255).astype(np.uint8)

        # Convert to BGR format for YOLO (expects 3-channel image)
        slice_bgr = cv2.cvtColor(normalized_slice, cv2.COLOR_GRAY2RGB)  # pylint: disable=no-member

        # Run YOLO prediction
        results = model.predict(slice_bgr, verbose=False)
        if len(results) == 0 or len(results[0].boxes) == 0:
            continue

        # Process detections
        h, w = slice_data.shape
        for box in results[0].boxes:
            # Get bounding box in YOLO format (normalized)
            x_center, y_center, width, height = box.xywhn[0].tolist()

            # Convert to pixel coordinates
            x1 = int((x_center - width / 2) * w)
            y1 = int((y_center - height / 2) * h)
            x2 = int((x_center + width / 2) * w)
            y2 = int((y_center + height / 2) * h)

            x1, y1 = max(0, x1), max(0, y1)
            x2, y2 = min(w, x2), min(h, y2)

            # Directly fill per-box region
            if axis == 0:
                binary_mask[i, y1:y2, x1:x2] = 1
            elif axis == 1:
                binary_mask[y1:y2, i, x1:x2] = 1
            else:
                binary_mask[y1:y2, x1:x2, i] = 1

    if verbose:
        # Print statistics
        tumor_voxels = np.sum(binary_mask)
        total_voxels = binary_mask.size
        tumor_percentage = (tumor_voxels / total_voxels) * 100

        print("Segmentation complete!")
        print(f"   Total voxels: {total_voxels:,}")
        print(f"   Tumor voxels: {tumor_voxels:,}")
        print(f"   Tumor percentage: {tumor_percentage:.2f}%")

    return binary_mask


def predict_mask(nifti_path, axis, verbose=False):
    """
    Generate a binary tumor mask from a 3D NIfTI image using a trained YOLO model.

    Args:
        nifti_path (str): Path to the input NIfTI file (e.g., FLAIR image).
        model_path (str): Path to the trained YOLO model (.pt file).
        conf_threshold (float): Confidence threshold for detections (default: 0.25).
        output_path (str, optional): Path to save the output mask. If None, saves next to input.

    Returns:
        str: Path to the saved binary mask NIfTI file.
    """

    assert axis in [0, 1, 2], "Axis must be 0 (sagittal), 1 (coronal), or 2 (axial)."

    # Load the NIfTI image
    nifti = nib.load(nifti_path)
    data = nifti.get_fdata()

    # Predict the binary mask
    if verbose:
        print("Generating tumor mask...")
    binary_mask = predict(data, axis, verbose)

    return binary_mask


def mask2cuboid_array(mask):
    """ Convert a binary mask to its bounding cuboid mask.
     Args:
         mask (np.ndarray): 3D binary mask.
     Returns:
         np.ndarray: 3D binary mask of the bounding cuboid.
     """
    coords = np.argwhere(mask)
    minz, miny, minx = coords.min(axis=0)
    maxz, maxy, maxx = coords.max(axis=0)
    new_mask = np.zeros_like(mask)
    new_mask[minz:maxz + 1, miny:maxy + 1, minx:maxx + 1] = 1
    return new_mask


def mask2cuboid_nifti(mask_path, output_path):
    """ Convert a binary mask NIfTI file to its bounding cuboid mask NIfTI file.
     Args:
         mask_path (str): Path to the input binary mask NIfTI file.
         output_path (str): Path to save the output bounding cuboid mask NIfTI file.
     Returns:
         str: Path to the saved bounding cuboid mask NIfTI file.
     """
    nifti = nib.load(mask_path)
    mask = nifti.get_fdata()
    cuboid_mask = mask2cuboid_array(mask)
    output_nifti = nib.Nifti1Image(cuboid_mask.astype("uint8"), nifti.affine, nifti.header)
    nib.save(output_nifti, output_path)


def unite_masks_array(*masks, method="union"):
    """
    Combine multiple binary masks into one using union or cuboid.

    Args:
        *masks (np.ndarray): Multiple binary masks to combine.
        method (str): Method to combine masks ('union' or 'cuboid').
    Returns:
        np.ndarray: Combined binary mask.
    """
    if method == "union":
        return np.clip(sum(masks), 0, 1)
    elif method == "cuboid":
        combined_mask = np.clip(sum(masks), 0, 1)
        return mask2cuboid_array(combined_mask)
    else:
        raise ValueError(f"Unknown combine method: {method}")


def unite_masks_nifti(mask_paths, output_path, method="union"):
    """
    Combine multiple binary mask NIfTI files into one using union or cuboid.

    Args:
        mask_paths (list of str): Paths to the input binary mask NIfTI files.
        output_path (str): Path to save the output combined mask NIfTI file.
        method (str): Method to combine masks ('union' or 'cuboid').
    Returns:
        str: Path to the saved combined binary mask NIfTI file.
    """
    masks = []
    for path in mask_paths:
        nifti = nib.load(path)
        mask = nifti.get_fdata()
        masks.append(mask)

    combined_mask = unite_masks_array(*masks, method=method)
    output_nifti = nib.Nifti1Image(combined_mask.astype("uint8"), nifti.affine, nifti.header)
    nib.save(output_nifti, output_path)
