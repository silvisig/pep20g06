# dictionare
empty_dict = {}
print(empty_dict)
print(type(empty_dict))

dict_with_values = dict(a='')  # a e o variabila in interiorul constr si nu putem avea o variabila cu numele 1
print(dict_with_values)
# putem avea doar stringuri ca si key primare

# my_dict ={1: 'a', 2: 'b'}
# print(my_dict)
# list1 = [1,2]
# list2 = [1,2,3]
# my_dict={list1: 'a', list2: 'b'}

my_str = 'abc'
print(dir(my_str))
# print(dir(my_str.__hash__())
# print(list1.__hash__())

print((1, 3, True).__hash__())
# obiectele care nu sunt mutuable nu pot fi folosite ca si kei  in dict
# obiectele mutuable pot fi folosite ca si key in dict

# muttable

new_dict = dict()
print(id(new_dict))
new_dict.update({'a': 'b'})
print(id(new_dict), new_dict)

# methods
print()
keys = new_dict.keys()
print(type(keys))
values = new_dict.values()
print(type(values), next(values.__iter__()))
items = new_dict.items()
print(type(items))

# unpack tuple
var1, var2, var3, *var4, var5 = (1, 2, 3, 4, 5, 6)
print(var1, var2, var3)
print(var4)
for x in [var4]:
    print(x)
    # get method and[]
    print(new_dict.get('a'))
    print(new_dict['a'])
    print(new_dict.get('b', 0))
    # remove key
    new_dict.pop('a')
    print(new_dict)

# exercitiu
mag1 = {'mere': 10, 'pere': 15, 'prune': 6, 'ananas': 20}
mag2 = {'mere': 11, 'pere': 15, 'prune': 6}
mag3 = {'mere': 10, 'pere': 16, 'prune': 7, 'papaya': 25}
lista_de_magazine = {'mag1': mag1, 'mag2': mag2, 'mag3': mag3}
lista_de_cumparaturi = {'mere': 2, 'pere': 3, 'prune': 6}


def best_buy(shops, shopping_list):
    totals = {}
    result = None
    totalcost = None
    for product, nr_items in shopping_list.items():
        for shop_name, shop_items in shops.items():
            cost = shop_items[product] * nr_items
            print(f'In {shop_name} object {product} costs: ', cost)

            totals.update({shop_name: totals.get(shop_name, 0) + cost})

    print(totals)
    for key, value in totals.items():

        if (totalcost is None) or (value < totalcost):
            result = key
            totalcost = value
    return result


print(best_buy(shops=lista_de_magazine, shopping_list=lista_de_cumparaturi))

#ex2: find prime number
def is_prime(number):

    for i in range(2, number//2 + 2):

       if not number% i :
           return False

    return True

print(is_prime(30))
print(is_prime(5))

def primes(limit):
    result =[]
    for i in range (limit):
        if is_prime(i):
            result.append(i)
    return result
print(primes(120))

#sets -acelasi tipuri de brackets ca la dict
my_set = set() #un set de elemente unice , nu putem sa avem acelasi el de 2 ori
my_set1 = {1,2,3,4,5}
print(type(set), my_set)
my_set2 = {1,3,5}
my_set2.update({7})
print(my_set2)
print(my_set2.pop())
print(my_set2.difference(my_set1)) #toate el care se gasesc in setu 2 si nu se gasesc in setul 1
print(my_set1.difference(my_set2))
#seturile : obiectele se autoaranjeaza in ordine crescatoare

print(my_set1.intersection(my_set2))
print(my_set1)
print(my_set2)#intersectia este aceeasi pt ambele seturi daca inversam
print(my_set1.symmetric_difference(my_set2)) #intersectia este aceeasi pt ambele seturi daca inversam
print(my_set2.symmetric_difference(my_set1))

#ex3

test_data = [[1,2,3],[3,3,5],[8,9,4]]
#union ->adauga un set la un nou set
test_data = [[1,2,3], [3,3,5], [8,9,4]]
def pinball_game_test(game_data, ful_range=10):
    range_values = set(range(1, ful_range + 1))
    ful_set = set()
    for mach_game in game_data:
        ful_set = ful_set.union(mach_game)
    return range_values.difference(ful_set)
print(pinball_game_test(test_data))


