# iterators

class ListIterator():
    def __init__(self, my_list: list):
        self.my_list = my_list

    def __next__(self):
        if len(self.my_list) == 0:
            raise StopIteration

        return self.my_list.pop(0)

    # o lista e un ob care se modifica , prin pop il modificam ,
    # prin lista tin o anumita stare despre ob meu
    # next returneaza cat si modifica atributul my_list care e o lista
    def __iter__(self):
        return self


# # deci se modifica si ob in sine.
# iterator = ListIterator([1, 2, 3])
# for i in interator:
#     print(i)
#
# print(iterator.__next__())
# print(iterator.my_list)
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
#
#
# # obiectul e modificat si ramane nemodificat
#
# class intIterator():
#     listed_number = []
#
#     def __init__(self, numar: int):
#         self.numar = numar
#         for i in range(1, self.numar + 1):
#             self.listed_number.append(i)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if len(self.listed_number) == 0:
#             raise StopIteration
#
#         return self.listed_number.pop(0)
# class IntObject():
#     def __init__(self,nr):
#         self.nr =nr
#   #  def __iter__(self):
#   #      return IntIterar
# int_object = IntObject(3)
#
#
# #lambda functions
#
# # o functie ce se scrie sub o alta forma
# def func1(a,b):
#     return a+b
# func1 = lambda a,b: a+b #returneaza ce e dupa :
# # folosesti obiectul functiei pt nu a mai consuma variabile si a nu mai salva in memorie
#
#
# #fctie lambda care primeste 1 arg si returneaza acel arg la putereaa2a
#
# func1= lambda x : pow (x,2)
# print (func1(3))
#
# #map functie+ob iterabil list string
# def process_chr(char:str):
#    chr( ord(char)+1)
text = 'my_test to process'
# result= map(process_chr,text)
# print(result)
# print(dir(result)) #ob poate fi itera cu for prin fiecare el din aceasta mapare
# for new_obj in result:
#      print(new_obj)

result = map(lambda char: chr(ord(char) + 1), text)
for new_obj in result:
    print(new_obj)

# o mapare intre o lista care contine primele 100 de nr si le mapez la nr respective /2
my_list = [x for x in range(100)]
for i in map(lambda k: k / 2, my_list):
    print(i)

# filter

list_number = [i for i in range(10)]
result = map(lambda k: k if k % 2 == 0 else None, list_number)
# result e un generator si se consuma odata ce a trecut prin for
for i in result:
    print(i)
result = filter(lambda a: a > 5, list(
    result))  # filter returrneaza obiectul , mapare intre valoare de adevar a functiei si returneaza sau nu obiectul din lista
for i in result:
    print(i)
# filtru pt un set de caractere si fiecare dntre caractere sa verfice daca char >m si daca da sa nu treaca de filtru

text = "".join([chr(i) for i in range(97, 123)])
print(text)
var = filter(lambda a: a > 'm', text)
for i in var:
    print(i)

# daca chr +1 >100
text = "".join([chr(i) for i in range(97, 123)])
var = filter(lambda a: ord(a) + 1 > 100, text)
for i in var:
    print(i)

# any- atata timp cat unu din ob iterabile e true
# any pt orice ob iterabil ca si un filstru care returneaza True doar daca unu din ob e TRUE
my_list = [1, 'a', True, False, False]
my_lis_F = [0, '', None, True, False, False]
print(any(my_list))
print(any(my_lis_F))

# all
# if all ob are true atunci e true , un ob nu e true,returneaza false
my_list = [1, 'a', True]
my_lis_F = [1, 'a', True, False]
print(all(my_list))
print(all(my_lis_F))


# inheretance-mostenire
class Wolf():
    bark = True

    def hunt(self):
        print('Hunting')
        raise NotImplemented  # cainele nu tre sa mosteneasca atributul vanatoare

    def method_1(self):
        pass


class Dog(Wolf):  # numele clasei care e mostenita

    def method_2(self):
        pass


dog = Dog()  # apelam clasa dog vin din metoda new si init
print('dog barks:', dog.bark)
dog.method_2()


class Animal(object):  # animal e o super clasa
    def __init__(self, species):
        self.species = species

    def hunt(self):
        print('nimic')


class Wolf(Animal):
    bark = True

    def __init__(self, species):
        super().__init__(species)

        self.attribute = 'wild'

    def hunt(self):
        print("hunting")

    #       raise NotImplemented
    def method_1(self):
        pass


class Coyote(Animal):
    bark = True

    def __init__(self, species):
        super().__init__(species)

        self.attribute = 'wild'

    def has_more_teeth(self):
        print('adaugam dintii')

    def hunt(self):
        print("hunting+")

    # raise NotImplemented

    def method_1(self):
        pass

class Car():

    __key = 123510
    _engine = 1.8
    def __init__(self, color):
        self.attribute = color
        self.__key = 7894
        self._engine = 2

    def start(self):
       self__engine_code = 12
       print('start')

class Dog(Coyote,Car, Wolf, Animal):  # stg la dreapta , first parintii next bunici etcpt mostenirept clase care au legatura, pt cele care n au leg ordinea n-are prioritate

    def __init__(self, species):
        super().__init__(species)
        self.attribute = 'domestic'

    #   def hunt(self):
    #     print('can t do that')

    def method_2(self):
        pass




dog = Dog('dog')
print('dog barks: ', dog.bark)
dog.method_2()
dog.method_1()
dog.hunt()
print(dog.attribute)
dog.has_more_teeth()  # apelam metoda din clasa coyote bicoz a mostenit atributele
dog.start()

class Suv(Car):
      def __init__(self,color, size):
          super(Suv,self).__init__(color)
          self.size = size
          self._Car__key = 12
          self._engine = 2

      def all_wheel_drive(self):
          print('activam 4X4')

suv = Suv("verde",12)
print(suv._Car__key)
print(suv._engine)#accesam variabile private
#atr private in clasa parinte pe self se pot modifica in cls respectiva __si numele var
#in clasa copil , self reprezinta cls copil ,pt modificarea var trebe numele cls parinte
suv.start()
print(suv._Car__engine_code)
suv._Car__engine_code = 20
print(suv._Car__engine_code)