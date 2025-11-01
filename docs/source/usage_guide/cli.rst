Command-Line Interface
======================

The ``neuroslice`` command provides a simple interface for brain tumor segmentation from the terminal.

Basic Syntax
------------

::

   neuroslice INPUT OUTPUT [OPTIONS]

**Required Arguments:**

* ``INPUT`` - Path to input FLAIR NIfTI file (.nii or .nii.gz)
* ``OUTPUT`` - Path to output mask NIfTI file

**Optional Arguments:**

* ``--axis`` - Slice direction (default: 1)
* ``--mode`` - Processing mode (default: union)
* ``--verbose`` - Show detailed progress

Simple Examples
---------------

Process with default settings::

   neuroslice FLAIR.nii.gz tumor_mask.nii.gz


Slice Direction Options
~~~~~~~~~~~~~~~~~~~~~~~

Use ``--axis`` to specify the slice orientation:

* axis=0: Sagittal (Left-Right)
* axis=1: Coronal (Front-Back), default
* axis=2: Axial (Top-Bottom)


.. code-block:: bash

   neuroslice input.nii.gz output.nii.gz --axis 0


More than one axis can be specified by providing a comma-separated list:

.. code-block:: bash

   neuroslice input.nii.gz output.nii.gz --axis 0,1,2

Processing Modes
~~~~~~~~~~~~~~~~


Union mode (default) creates a mask with only the detected tumor regions:

.. code-block:: bash

   neuroslice input.nii.gz output.nii.gz --mode union

Cuboid Mode
~~~~~~~~~~~

Creates a bounding box around all detections (better for downstream processing as it provides a convex region):

.. code-block:: bash

   neuroslice input.nii.gz output.nii.gz --mode cuboid

Complete Example
~~~~~~~~~~~~~~~~

Process with all options specified:

.. code-block:: bash

   neuroslice brain_scan.nii.gz result_mask.nii.gz --axis 2 --mode cuboid --verbose



.. note::
   
   * Try different orientations if results are suboptimal
   * Use ``--verbose`` during initial testing
   * Consider using cuboid mode for downstream processing
