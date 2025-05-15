'''
    VIRTUAL ENVIRONMENT

    A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing you to work on multiple projects that have conflicting packages without conflicts
    This can be specially useful when working on projects that have conflicting package version that are not compatible with each other

        # create a virtual environment
                python -m venv myenv
        
        # activate the virtual environment (Linux/macOS)
                source myenv/bin/activate
        
        # activate the virtual environment (cmd terminal windows)
                myenv\Scripts\activate.bat
        
        # activate the virtual environment (powershell windows)
                myenv\Scripts\activate.ps1
        
        # deactive virtual environment
                deactivate


                
    The "requirement.txt" file

        In additon to creating and activating a virtual environment, it can be useful to create a requirements.txt file that lists the packages and their versions that your project depends on. This file can be used to easily install all the required packages in a new environment

            # Lists all packages and their versions
                    pip freeze

            # Output the list of installed packages and their versions to a file by creating that file
                    pip freeze > requirements.txt

            # Install all of the packages listed in the requirements.txt file at once
                    pip install -r requirements.txt

    NOTE: Using virtual environments and a requirements.txt file can help you manage the dependencies dor your Python projects and ensure that your projects are portable and can be easily set up on a new machine
'''
import pandas as pd
print(pd.__version__)