print('hello world')
print('hello world', sep='--')
print('hello world', 'hello', 'what', end='$\n')

hello = 'hello world'
#hello este o variabila precum si print
print(hello)
 #in py avem obiecte putem printa print
 #indentation error- nu incepem cu spatiu pe linie

print('silvia', end='*\n')
number1 = 12
number2 = 13
number3 = number1+number2
print(number3)
number4 = number1 - number2
print(number4)
print()
number1 = 12
number2 = '13'
#number3 = number1/number2
print(number3)
print(dir(number1))
#dir  e o fctie care raspunde cu ceva dar eu nuf ac nimic cu acel raspuns si as vrea sa vdm cu ce raspundem
print(dir(number2))

#erorile nu se vad mereu in acelasi timp-> 2 canale de comunicare <stdout>
# si stderr ,deci daca aj outputu primu, nu vedem msj de eroare

number1.__add__(2)
print(number1.__add__(2))