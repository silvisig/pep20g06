#sleep

import time #desi este un packet,devine un obiectcandil apelam

print(time)
print(time.sleep(1))

#putem importa tot modulul sau doar o clasa

from time import sleep # am importat direct fctia sleep din packetul time
#si oriunde am scrie sleep stie sa se refere la acel sleep importat
print('sleeping 1 sec')
sleep(1)

def sleep(seconds):
     print('do nothing for {seconds}')
     print(sleep(10))
 #importam sub un alt nume
from time import sleep as imported_sleep

print(imported_sleep)

#our module

import communicator
import sys
print(sys.path)
#toatepathurile dupa import

#add to path
#sys.path.append()
#aici adaugam proiectul diferit

#use communicator ,cand importam ,se uita in fisierul init,sitoate obievteledin el devin obiecteinnamespaceul lui pysivastiisa lefoloseasca ulteiror


print(communicator.var1)
print(communicator.is_prime(19))

import datetime
from time import sleep, time , strftime
def my_time() :
     result = []
     time1=str((datetime.time(19, 30, 22)))
     time2=(strftime('%H:%M:%S'))
     print(time2.split(':'))
     for i in range (3):
         result.append (str(int(time2.split(':')[i]))- (int(time1.split(':')[i])))
   #    print(result)

#tema : return ":".join(result) conditie pt valoare negativa



#print(time())
#print(strftime('%H:%M:%S' ))

#factorial

def factorial(n):
     result = 1
     for i in range (1, n+1):
          result *= i
     return result
print(factorial(3))

def factorial(n):
     if n == 0:
          return 1
     else:
          return  n * factorial(n-1)
     print(factorial(3))



my_list =[[1,[2,[3]]],  [4,[5,[6]]],[7,[8,[9]]]]
print( isinstance(my_list,list ))
print(type(my_list) == list)
print(type(3) == list)

#extragere de nr intr-o sg lista

def flatten_list(list_to_flatten):
     result = []
     for inner_object in list_to_flatten :
          if isinstance(inner_object , int) :
               result.append(inner_object)
          else:
               result += flatten_list(inner_object)

     return result
print(flatten_list(my_list))

def flatten_list_to_tupple(list_to_flatten):
     result = []
     for inner_object in list_to_flatten :
          if isinstance(inner_object , int) :
               result.append(inner_object)
          else:
               result += flatten_list(inner_object)

     return tuple(result) #s-a modificat tot resultul din toate fctiile
#print(flatten_list_to_tuple(my_list))
#am folosit liste dar resultatul e un tuple.felul in cre modificam raspunsul
#afecteaza codul, si fiecare raspuns din fiecare apelare recursiva

def flatten_list_to_tuple(list_to_flatten):
    result = []
    for inner_object in list_to_flatten:
        if isinstance(inner_object, int):
            result.append(inner_object)
        else:
            result += list(flatten_list_to_tuple(inner_object))
    return tuple(result)
#variables (global, non-local, local)
var1 = 'my var to print'
def outer(arg1):
     def inner(arg2):
          pass
     return inner
x = (outer(10))
var1 = 'my new var to print'
x(10)
#o pers cu unkown nam

def conversation():
    name_ = ''
    def hello(name='sir'):
        nonlocal name_
        name_ = name
        name_ = input(f'hello {name}:')
    def question(q='question'):
        print(f'{name_}, {q}?')
    hello()
    return question

object = conversation()
object('what is that')