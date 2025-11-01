Troubleshooting
===============

Installation Errors
-------------------

If you encounter intallation errors due to incompatible dependencies, check whether you have python 3.8 or higher installed. You can create a virtual environment to isolate the installation.

Using venv:

.. code-block:: bash

   python -m venv neuroslice_env
   source neuroslice_env/bin/activate 
   pip install neuroslice

Using conda:

.. code-block:: bash
   
   conda create -n neuroslice_env python=3.8
   conda activate neuroslice_env
   pip install neuroslice


Model Download Issues
---------------------

Models are downloaded from Hugging Face on first use. 
So, if you face issues related to model downloads, ensure that you have a stable internet connection.

Contact and Support
-------------------

If you need further assistance, please open an issue on the `GitHub repository <https://github.com/anamatoso/neuroslice/issues>`_.