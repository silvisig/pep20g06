#functii

def my_print(value):
    print( type(value))
    print(value)
    my_print('hello world')
#return
print()
print()
def add_numbers(nr1, nr2):
    result =nr1 +nr2
    print(result)
    return result
sum = add_numbers(1,2)
print(type(sum))




def pow(x, y):
    x = 3
    y = 2
    result= pow(x,y)
    return result

# def power(x, y):
#return  x**async nr_pow=poer(2,3)

print(add_numbers)
print(dir(add_numbers))
print(add_numbers.__call__(1,2))
#function e un obiect cu o metoda call

for i in range(0,3):
    def add_numbers(nr1, nr2):
        result = nr1 + nr2
        print(result)
        return result
    print(add_numbers)
    #putem sa definim o functie in interiorul alteia=
    #=nested functions
number2 =10
def outside(number):
    def inside():
        return number +number2
    return inside
var1 = outside(10)
print(type(var1))
number2 =11
print(var1())
#atatea functii cate argumente is date in functia initiala

def function(*args):
     list1 = []
     for i in args:
         def infction():
             print(i)
             list1.append(infction)
     return list1
var1=function('a','b','c')
print(var1)

#lists
#seturi de obiecte, mai multe obiecte in alt obiect si avem referinta la toae obiectele
empty_list =[]
print(empty_list)
empty_list= list()

var1=3

print(id(empty_list))
empty_list.append(1)
print(dir(empty_list))
empty_list.append(True)
print(empty_list)
print(id(empty_list))
empty_list.append(var1)
print(id(empty_list))
#pot fi moddificate dar raman in acelasi loc in memorie

var1 =4
print(id(empty_list))
empty_list.append(var1)
#pointerii din lista se refera la adrese unde sunt salvate obiecte
#pt un ob mutabil daca adaugam in lista o alta lista


my_list_outside =[]
my_list_outside.append(1)
my_list_inside = []
my_list_outside.append(my_list_inside)
my_list_inside.append(2)
print(my_list_outside)
my_list_inside.append(3)
print(my_list_outside)

#tuple virgula dintre obiecte chair daca exista doar un ob tre sa punem virgula

empty_tuple = tuple()
one_object_tuple = (1,)
two_object_tuple = (1,'a')

no_brackets_tuple= 1 ,'a', True
print(type(no_brackets_tuple))
print(no_brackets_tuple)

#tuple nu este mutabil, orice modificare se face trebuie definit alt obiect

new_two_object_tuple = (1,'a')
print(id(two_object_tuple)), id(new_two_object_tuple)
new_two_object_tuple += None,
print(new_two_object_tuple)

#un text primit ca argument si salveaza fiecare nr de caracter intr-o lista
def function(string,key):
    list1 = []
    for i in string:
        list1.append (chr(ord(i).__xor__(key)))
    return ''.join(list1)
encrypted= function('hello world', 140)
print(encrypted)
decrypted =function(encrypted,140)
print(decrypted)



#return o lista cu toate  nr aferente literelor
     #numerele coresp literelor
#bit operations

result = 1 and 0 #classical
print(result)
result = 1& 0 #bit
print(result)

result = 2 and 3 #classical
print(result)
result = 2& 3 #bit
print(result)

result = 3 and -1 #classical
print(result)
result = 3& -1 #bit
print(result)
print(-1 ^3)
print((-1).__xor__(3))
print(3|3)
print(~3)



