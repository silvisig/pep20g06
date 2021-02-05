my_list=[ 1, 2 , 3]



my_list_iter = my_list.__iter__()

print(my_list_iter)
print(next(my_list_iter))
print(next(my_list_iter))
#print(len(my_list_iter))

#generator

def my_generator():

    for  i in range(3):
     print('before')
     yield i
     print('after')

gen = my_generator()
print(type(gen))
print(gen.__next__())
print('step1')
print(gen.__next__())
print('step2')
print(gen.__next__())
print('step3')

#list comprehension
my_gen= (i for i in range(3))
print(my_gen)#pt fiecare i din acest for adauga-l la lista
my_gen =(i for i in [1 , 2, 3])
print(my_gen.__next__())

#generator care prodice numere impare
print('Iata codul')

my_var=(i for i in range(10) if i %2 !=0) #variabila care poiunteaza catre generator
print(my_var.__next__())
print(my_var.__next__())
