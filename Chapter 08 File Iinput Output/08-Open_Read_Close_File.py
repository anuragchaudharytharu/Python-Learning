'''
    Open, Read & Close File

    We have to open a file before reading or writing
        Syntax:
                open_file = open("file_name", "mode")
                            NOTE: By default it's in read text mode if we donot provide mode

                read_file = file.read()

                close_file = file.close()
                            NOTE: We must always close the file if we open the file. This is so that others cannot access it and change it

                
            "mode":
                    "r" ====> open for reading (default). The stream is positioned at the beginning of the file

                    "r+" ====>  open for reading and writing. Overwrites but doesnot delete truncate. The stream is positioned at the beginning of the file

                    "w" ====> open for writing, truncating i.e overwriting the file first. It's also used to create a file

                    "w+" ====> open for reading and writing, truncating i.e overwriting the file first. It's also used to create a file. The stream is positioned at the beginning of the file

                    "x" ====> create a new file and open it for writing

                    "a" ====> open for writing, appending to the end of the file if it exists. It's also used to create a file if the file doesn't exist.  The stream is positioned at the end of the file

                    "a+" ====> open for reading and writing. Appending to the end of the file if it exists. It's also used to create a file if the file doesn't exist. The stream is positioned at the end of the file
                    
                    "b" ====> binary mode

                    "t" ====> text mode (default)

                    "+" ====> open a disk file for updating (reading and writing)

            "file_name":
                    example ====>  sample.txt, demo.docx

    
    NOTE: 
        Pointer/cursor stream is placed the beginning of the file. For Reading and Writing, pointer positioned at the start of the file. For append, pointer positioned at the end of the file

        They depend upon the pointer position

        When we read the entire file, that pointer moves to the end of the file line. So when we read the file again, it gives a empty line as a read content as it start to read the file from the next line in which there is no content.
'''


# .read() ======> reads entire file
file = open("demo.txt", "rt")
data = file.read()
print(data)
print(type(data))
close = file.close()

# read upto certain number of charcters
open_file = open("demo.txt", "rt")
read5Char = open_file.read(5)
print(read5Char) # I am 
close_file = file.close()

# .readline() =====> reads One line at a time
openFile = open("demo.txt", "rt")
line1 = openFile.readline()
print(line1) # I am learning python
line2 = openFile.readline()
print(line2) # from Harvard Introduction to programming with Python
closeFile = file.close()