Getting Started
===============

Neuroslice provides two interfaces for brain tumor segmentation:

1. **Command-Line Interface (CLI)** - Quick processing from the terminal
2. **Python** - Integration into your scripts and pipelines

Both interfaces provide access to the same core functionality, allowing you to choose based on your workflow preferences.

Quick Examples
--------------

Command-line
~~~~~~~~~~~~
::

   # Basic usage
   neuroslice FLAIR.nii.gz tumor_mask.nii.gz
   
   # With options
   neuroslice FLAIR.nii.gz tumor_mask.nii.gz --axis 2 --mode cuboid --verbose

Python
~~~~~~
::

   from neuroslice import predict_mask
   import nibabel as nib
   
   # Generate mask
   mask = predict_mask("FLAIR.nii.gz", axis=2, mode="cuboid", verbose=True)
   
   # Save output
   nifti = nib.load("FLAIR.nii.gz")
   output = nib.Nifti1Image(mask.astype("uint8"), nifti.affine, nifti.header)
   nib.save(output, "tumor_mask.nii.gz")

.. note::
   
   * Try different orientations if results are suboptimal
   * Use verbose during initial testing
   * Consider using cuboid mode for downstream processing

See also
--------

* :doc:`cli` - Detailed command-line usage
* :doc:`python` - Python examples
* :doc:`../commands` - Complete command reference