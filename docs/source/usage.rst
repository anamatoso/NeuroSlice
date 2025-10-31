Usage Guide
===========

Command Line Interface
----------------------

Basic usage:

.. code-block:: bash

   neuroslice input.nii.gz output_mask.nii.gz

With options:

.. code-block:: bash

   neuroslice input.nii.gz output_mask.nii.gz --axis 2 --mode cuboid --verbose

Python API
----------

Generate a tumor mask:

.. code-block:: python

   from neuroslice import predict_mask
   import nibabel as nib

   mask = predict_mask("input.nii.gz", 1, verbose=True)
   
   nifti = nib.load("input.nii.gz")
   output = nib.Nifti1Image(mask.astype("uint8"), nifti.affine, nifti.header)
   nib.save(output, "output_mask.nii.gz")