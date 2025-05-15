'''
    DELETING a File
    
    To delete a file, We need to use "os" module
                            import os
                            os.remove(file_name)

            MODULE: Module (like a code library) is a file written by another programmer that generally has a function we can use. We terminal to install module        
                    To install module:
                            pip install module_name

    NOTE: we cannot delete a file like we do for reading and writing a file
'''

import os

os.remove("sample.txt")