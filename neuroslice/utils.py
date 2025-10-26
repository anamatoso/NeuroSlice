from huggingface_hub import hf_hub_download
from huggingface_hub.utils import disable_progress_bars


def download_model(axis, verbose):
    """ Download the YOLO model for the specified direction from Hugging Face Hub.
     Args:
         direction (str): Direction of slices ('coronal', 'sagittal', 'axial').
         verbose (bool): Whether to show download progress.
     Returns:
         str: Path to the downloaded model file.
     """

    assert axis in [0, 1, 2], "Axis must be 0 (sagittal), 1 (coronal), or 2 (axial)."
    if axis == 0:
        direction = "sagittal"
    elif axis == 1:
        direction = "coronal"
    elif axis == 2:
        direction = "axial"

    if not verbose:
        disable_progress_bars()
    if verbose:
        print("Downloading model...")
    model_path = hf_hub_download(
        repo_id="anamatoso/neuroslice",
        filename=f"models/{direction}_best.pt",
    )
    return model_path
