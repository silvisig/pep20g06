#fisiere
from time import sleep
file = open('my_Text','w')
file.__enter__()
file.__exit__()
print(type(file))
#file.write('new text')
file.close()

sleep(20)
with open('my_Text','w') as file:

  file.write('my text24352352')
import logging
class FileWriter():
    def __init__(self,file_path):
        self.file_path = file_path



    def __enter__(self):
       self. file = open(self.file_path,'x')
       return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.write('\n')

        self.file.close()
        print(exc_type,exc_val,exc_tb)

with FileWriter('new_file') as  file:
    file.write('text nou')




class FileWriter():
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.file = open(self.file_path, 'x')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.write('\n')
        self.file.close()
       # return True


with FileWriter('new_file') as file:

    var =int( input(">>>"))
    while var :

     var2 = input("...")
     file.write(str(var) + ("\n" if var2 else ""))
     var = int(var2)

import logging
class FileWriter():
    def __init__(self, file_path):
        self.file_path = file_path
    def __enter__(self):
        self.file = open(self.file_path, 'x')  # creaza fisier
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.write('\n')
        self.file.write(str(exc_tb.tb_frame).split(',',1)[1])
        self.file.close()
        return True

with FileWriter('new_file') as file:
    my_string = int(input(">>>"))
    while my_string:
        my_string2 = input("...")
        file.write(str(my_string) + ("\n" if my_string2 else ""))
        my_string = int(my_string2)