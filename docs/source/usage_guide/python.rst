Python
==========

Neuroslice provides a Python API for integration into your scripts and processing pipelines.

Core Functions
--------------

The main functions available are:

* ``predict()`` - Generate mask from array data
* ``predict_mask()`` - Generate mask from NIfTI file
* ``predict_multi_axis()`` - Process multiple orientations
* ``mask2cuboid()`` - Convert mask to bounding cuboid
* ``unite_masks()`` - Generate the union of multiple masks

Basic Usage
-----------

Generate Mask from File
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from neuroslice import predict_mask
   import nibabel as nib
   
   # Generate mask
   mask = predict_mask("input.nii.gz", axis=1, verbose=True)
   
   # Save output
   nifti = nib.load("input.nii.gz")
   output = nib.Nifti1Image(mask.astype("uint8"), nifti.affine, nifti.header)
   nib.save(output, "output_mask.nii.gz")

Process from Array
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from neuroslice import predict
   import nibabel as nib
   
   # Load data
   nifti = nib.load("input.nii.gz")
   data = nifti.get_fdata()
   
   # Generate mask
   mask = predict(data, axis=1, verbose=True)

Advanced Usage
--------------

Multiple Orientations
~~~~~~~~~~~~~~~~~~~~~

Process along multiple axes and combine results:

.. code-block:: python

   from neuroslice import predict_multi_axis
   import nibabel as nib
   
   # Load data
   nifti = nib.load("input.nii.gz")
   data = nifti.get_fdata()
   
   # Process multiple axes
   mask = predict_multi_axis(data, axis=[0, 1, 2], verbose=True)
   
   # Save result
   output = nib.Nifti1Image(mask.astype("uint8"), nifti.affine, nifti.header)
   nib.save(output, "combined_mask.nii.gz")

Or using predict_mask:

.. code-block:: python

   from neuroslice import predict_mask
   
   # Process multiple axes directly
   mask = predict_mask("input.nii.gz", axis=[0, 1, 2], verbose=True)

Convert to Cuboid
~~~~~~~~~~~~~~~~~

Convert a mask to its bounding cuboid:

.. code-block:: python

   from neuroslice import mask2cuboid
   
   # Convert existing mask
   cuboid_mask = mask2cuboid(mask)

Combine Multiple Masks
~~~~~~~~~~~~~~~~~~~~~~

Unite masks from different processing runs:

.. code-block:: python

   from neuroslice import unite_masks
   
   # Generate masks from different orientations
   mask1 = predict(data, axis=0, verbose=False)
   mask2 = predict(data, axis=1, verbose=False)
   mask3 = predict(data, axis=2, verbose=False)
   
   # Combine using union
   combined = unite_masks(mask1, mask2, mask3)

Complete Workflow Example
-------------------------

Processing Pipeline
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import nibabel as nib
   from neuroslice import predict_mask, mask2cuboid
   from pathlib import Path
   
   def process_brain_scan(input_path, output_dir, use_cuboid=False):
       """
       Process a brain scan and save the tumor mask.
       
       Args:
           input_path: Path to input NIfTI file
           output_dir: Directory to save output
           use_cuboid: Whether to use cuboid mode
       """
       # Create output directory
       output_dir = Path(output_dir)
       output_dir.mkdir(parents=True, exist_ok=True)
       
       # Generate mask
       print(f"Processing {input_path}...")
       mask = predict_mask(input_path, axis=1, verbose=True)
       
       # Convert to cuboid if requested
       if use_cuboid:
           mask = mask2cuboid(mask)
       
       # Save output
       input_name = Path(input_path).stem.replace('.nii', '')
       output_path = output_dir / f"{input_name}_mask.nii.gz"
       
       nifti = nib.load(input_path)
       output = nib.Nifti1Image(mask.astype("uint8"), nifti.affine, nifti.header)
       nib.save(output, output_path)
       
       print(f"Mask saved to: {output_path}")
       return mask
   
   # Use the function
   mask = process_brain_scan("brain.nii.gz", "results", use_cuboid=True)


See Also
--------

* :doc:`../commands` - Complete API documentation
* :doc:`cli` - Command-line interface usage