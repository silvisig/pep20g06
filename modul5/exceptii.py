# exceptii
from time import sleep

var = 2
try:
    sleep(3)
    result1 = 2 / '0'
    if var == 0:
        result2 = 2 / var
except Exception:
    print('smthin is wrong')
except TypeError:
    print('Bad operand')
except ZeroDivisionError:
    print('bad division')
else:
    print('this will only execute no exception')
finally:
    print('this will always be executed')
    # function input de la tast daca primeste orice altceva decat un nr atunci sa ne dea un mesaj , daca
    # daca primeste nr sa-l imparta la 2


def div(divider=2):
    if divider == 0:
        raise AttributeError('nu e ok sa fie 0 ')
        if divider % 2 == 1:
            raise AttributeError('nu e div cu 2')
        var1 = input("Give number: ")
        try:
            return int(var1) / 2
          except ValueError:
            print('Wrong var type')
          except TypeError:
            print('wrong var type')


print('Wrong var type')

print(div(2))
try:
    div(3)
except AttributeError as e:
    print('try  again')
    if e.args[0] ==  'nu e div cu 2':
        print('iata exceptia')


# def function care da o eroare specificata de noi


def check_if_not_0(nr=0):
    if nr == 0:
        raise ValueError('number is 0')
    print('value is not 0')
    if nr == 10:
        raise ValueError
    check_if_not_0(nr=1)


check_if_not_0(nr=1)
print('ceva')
try:
    check_if_not_0()
except ValueError as e:
    print('mai incercam ')
    if e.args[0] == 'number is 0':
        print('Iata exceptia')
    else:
        raise e

AttributeError('bad number')

def div(divider=2):
    if divider == 0:
        raise AttributeError('nu e ok sa fie 0 ')
    if divider % 2 == 1:
        raise AttributeError('Not divisible with 2','Value 2 of Attribute Error')
    var1 = input("Give number: ")
    try:
        return int(var1) / 2
    except ValueError:
        print('Wrong var type')
    except TypeError:
        print('Wrong var type')

print(div())
try:
    div(3)
except AttributeError as e:
    print('Try again')
    if e.args[0] == 'Not divisible with 2' and e.args[1]=='Value 2 of Attribute Error':
        print('This is my exception')

#class

#model dupa care putem sa facem o masina,un pattern
class CarFactory():
    model = volvo
    def __init__(self): #constructorul clasei
        print('building car')
        self.color = 'green'

    def __le__(self,second_car):
        print('yes it is',second_car)
        return id(self) <= id (second_car)
car1 = CarFactory()
car2 = CarFactory()
print('class atribute', CarFactory.model)
print('instance variable:', car1.model)
print(car1.color)
#print(car1)
#print(car2)

#print(car1 <= car2)
print(car1 <= car1)
#print(car

#muttable class attributes
class A:
    muttuable_obj = []
    def change_attr(self,value):
        self.muttuable_obj.append(value)
a= A()
print(a.muttuable_obj)
a.change_attr(1)
print(a.muttuable_obj)

b= A()
print(b.muttuable_obj)
b.change_attr(2)
print(b.muttuable_obj)

print()
print(a.muttuable_obj)
#numara cate masini au fost construite .counter

class Factory:
    _counter = [0]
    def __init__(self):
        self._counter.append(self._counter.pop(0) + 1)

first_car = Factory()
second_car = Factory()
print(Factory._counter)


class A:
    __attr0 ='really hide' # __private
    _attr1 = 'hide' #_ protected
    attr2 = 'do not hide'

a = A()
print(a.__attr0)
print(a._attr1)
print(a.attr2)
