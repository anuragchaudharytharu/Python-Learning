'''
    del Keyword

        used to delete object attributes/properties or object itself
                        del s1.name
                        del s1
'''

class Student:
    def __init__(self, fullName, description):
        self.name = fullName
        self.delete = description

s1 = Student("Klien", "He is THE FOOL who rules the black fog")

print(s1.delete)
del s1.delete
print(s1.delete)