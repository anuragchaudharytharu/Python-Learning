'''
    WRITING to a file

    Create/Overwrites the entire file with new content/line/data

    Syntax:
            for "mode" == "w" (i.e overwrite):
                        f = open("file_name", "w")
                                        #overwrites the entire file. If file doesnot exist, it creates new file

                        f.write("this is the new content/line/data")
            
            for "mode" == "a" (i.e append):
                        f = open("file_name", "a")
                                        #Adds to end of the existing file. If file doesnot exist, it creates new file

                        f.write("this is the new content/line/data")    
'''

# create a new file
newFile = open("sample.txt", "w")
newFile.close()

# overwrite the file with new content
file = open("sample.txt", "w")
file.write("I want to learn machine learning and get a job")
file.close()

# append/adds content to the end of the existing content
f = open("sample.txt", "a")
f.write("\nAfter that, I want to be among the top AI Researcher in the world")
f.close()