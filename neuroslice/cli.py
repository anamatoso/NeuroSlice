import argparse
from pathlib import Path
import nibabel as nib
from .core import predict_mask, mask2cuboid_array


def main():
    parser = argparse.ArgumentParser(
        description="Neuroslice: Brain tumor segmentation using YOLO"
    )
    parser.add_argument(
        "input",
        type=str,
        help="Path to input NIfTI file (.nii or .nii.gz)"
    )
    parser.add_argument(
        "output",
        type=str,
        help="Path to output mask NIfTI file"
    )
    parser.add_argument(
        "--mode",
        type=str,
        default="union",
        choices=["union", "cuboid"],
        help="Processing mode: union or cuboid (bounding box)"
    )
    parser.add_argument(
        "--axis",
        type=int,
        default=1,
        choices=[0, 1, 2],
        help="Slice direction for single-direction mode (default: 0 = coronal)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print detailed statistics"
    )

    args = parser.parse_args()

    # Validate input file exists
    if not Path(args.input).exists():
        print(f"Error: Input file '{args.input}' not found.")
        return 1

    # Load NIfTI for later saving
    nifti = nib.load(args.input)

    mask = predict_mask(args.input, args.axis, verbose=args.verbose)

    if args.mode == "cuboid":
        final_mask = mask2cuboid_array(mask)
    else:
        final_mask = mask

    # Save output
    output_nifti = nib.Nifti1Image(final_mask.astype("uint8"), nifti.affine, nifti.header)
    nib.save(output_nifti, args.output)
    if args.verbose:
        print(f"Mask saved to: {args.output}")

    return 0


if __name__ == "__main__":
    exit(main())
