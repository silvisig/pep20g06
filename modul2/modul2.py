# binary numbers
# 1=0b0001
# 2=0b0010

# hexadecimal
# 1=0o001
# 2=0o002
print(0o17)
print(0x11)
print(123e6)

# operatii aritmetice
# #x/y impartirea cu virgula
number1 = 3
number2 = 4
print('impartire 3/4:', number1 / number2)
print('floordiv4/3', number1 // number2)  # partea intreaga din nr respectiv care rezulta la impartire
print('remander 4%3', number1 % number2)  # restul impartirii
print('negative 3:', -number1)
print('zero:', number1 + number2)
print('3 to the power of 4:', number1 ** number2)

a = 3
b = 4
c = 5
result = (-b + pow((b ** 2) - 4 * a * c, 1 / 2)) / (2 * a)
print(result)

number4 = 0.75
number5 = 1.0 + 2.3j  # j e pt nr complexe nu conteaza daca e j mare sau j mic
print(type(number4))
print(type(result))
print(type(number5))

# string:
# orice tip de ghilimea e suportata inclusiv seturi de 3 """
string5 = 'hello world'
string5 = "hello world"
string5 = '''hello world'''
string5 = " " "hello world"""
print(string5)
string5 = u'hello \nworld'
string5 = r'hello \n world'  # caracterele nu sunt interpretate  pt caractere speciale deci \n nu mai e interperetat ca si linie noua
print(string5)
string5 = f'hello : {string5}'
print(string5)  # string formatabil , daca il luam si il printam nu se vede nici o diferenta
# daca pune{} in interior putem sa dam obiecte printate
# ctrl+alt +l pt aranjare a codului automata
result = string5[4]
print(string5)
result = string5[-3]
result = string5[
         4:7]  # interval inchis in stg si deschis in dreapta deci nu include caracterul de la index 7 nu e cuprins
# totul pana la caracter cu index 7
print('citim linia care trebuie?', result)
result = string5[4:7:1]  # ultimul e stepul/hop , step de 1 inseamna fiecare caracter 2 din 2 in 2
print(result)
restult = string5[-2:-6:-2]
print(result)
# citirea se face doar in ordine de la stg la dr. deci un interval 9:4 nu exista returneaza 0
## String interpretation:
string5 = u'Hello\nWorld'
print('unicode string:', string5)
string5 = r'Hello\nWorld'
print('Row string:', string5)
string5 = f'Hello World: {string5}'
print('Formatted string:', string5)

#dot notation for strings:

print('string actions', dir(result)) # dir trebuie printat altfel nu vedem nimic
 #functia de lower se acceseaza din obiect folosind .
print(result.upper()) #toate caract in litere mari
print(result.capitalize()) #primu caract litera mare, restu litere mici
#join are nevoie de o lista de obiecte sau de un ob iterabil
result= result + '{}'
print(result.format('silvia'))
print(result.format(6, 'silvia'))
#metoda -trebuie sa-i dam un argument ca sa functioneze
print(result.find('h'))
print(result.center(20, '#'))
# dot notation for ints:

print(number1.__add__(number2))
print((3).__add__(4))
print(number1.__mul__(number2)) #multiply
print(number1.__truediv__(number2)) #division
#obiectele au diverse actiuni-metode si fctii e pot fi apelate cu .dot notaions
print('power of:', number1.__pow__(number2)) #ridicare la putere

