# 3. Write a program to print contents of a directory using the os module. Search online for the function which does that
import os

def print_directory_contents(path):
    try:
        # List all files and directories in the given path
        contents = os.listdir(path)
        
        print(f"Contents of directory '{path}':")
        for item in contents:
            print(item)
    
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = input("Enter the directory path: ")
print_directory_contents(directory_path)