Welcome to Neuroslice
=====================

**Neuroslice** is a Python package for brain tumor segmentation using the YOLOv11m model on MRI FLAIR data.


Overview
--------

Neuroslice provides automated brain tumor bounding box detection using pre-trained YOLO models. It processes FLAIR MRI images slice-wise and supports three slice orientations (coronal, sagittal, and axial). Models are automatically downloaded from Hugging Face when first used.

Quick Start
-----------

Install via pip:

.. code-block:: bash

   pip install neuroslice

Basic usage:

.. code-block:: bash

   neuroslice input.nii.gz output_mask.nii.gz --axis 0 --mode --verbose

.. warning::
   
   Only use FLAIR sequences as the model was trained only on FLAIR data.

Table of contents
=================

.. toctree::
   :maxdepth: 1
   :caption: Installation
   
   installation/installation_guide.rst
   installation/troubleshooting.rst

.. toctree::
   :maxdepth: 1
   :caption: Usage Guide
   
   usage_guide/index
   usage_guide/cli
   usage_guide/python

.. toctree::
   :maxdepth: 1
   :caption: Additional Information

   commands
   contributing
   citation
