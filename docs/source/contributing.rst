Contributing
============

Contributions to Neuroslice are welcome! This page provides guidelines for contributing to the project.

How to Contribute
-----------------

1. **Fork the Repository**

   Fork the repository on GitHub at https://github.com/anamatoso/neuroslice

2. **Clone Your Fork**

   .. code-block:: bash

      git clone https://github.com/YOUR-USERNAME/neuroslice.git
      cd neuroslice

3. **Create a Branch**

   .. code-block:: bash

      git checkout -b feature/YourFeatureName

4. **Make Your Changes**

   Make your changes (i.e. add new feature or correct bug) in the codebase.
   Always follow the existing code style.
   Update the documentation accordingly

5. **Check if it follows code style guidelines**

   Install flake8 and pylint if you haven't already:

   .. code-block:: bash

      pip install flake8 pylint

   Run the checks (Flake and Pylint checks should pass without errors (and with score>=7.0 for pylint)):

   .. code-block:: bash

      flake8 . --count --max-complexity=10 --max-line-length=127 --statistics
      pylint $(find . -type f -name "*.py" ! -path "*/venv/*" ! -path "*/.venv/*" ! -path "*/env/*") --fail-under=7.0 --max-locals=30

6. **Commit Your Changes**

   .. code-block:: bash

      git add .
      git commit -m "Add: Brief description of your changes"

7. **Push to Your Fork**

   .. code-block:: bash

      git push origin feature/YourFeatureName

8. **Open a Pull Request**

   Go to the original repository and open a Pull Request with a clear description of your changes.




Code Style Guidelines
---------------------

* Follow PEP 8 style guidelines
* Use meaningful variable and function names
* Add docstrings to all functions (Google style preferred)
* Update documentation as needed
* Keep functions focused and modular

Reporting Issues and Questions/Support
--------------------------------------

1. Check existing issues to avoid duplicates
2. Open a new issue on GitHub
3. Provide clear description and steps to reproduce (if applicable)
4. Include system information and error messages if applicable
5. Add an appropriate label (bug, enhancement, question, etc.)
