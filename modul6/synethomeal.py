import datetime

class Food(object):  #
    def __init__(self, species=None, time=None,diff=None):
        self.species = species #types of food in the fridge
        self.time=time #time for mealprep
        self.diff =diff #difficulty rankingg

   # def veggies(self):
   #     print('nimic')


#class Spanac(Food):
#    greenvegies = True

#    def __init__(self, species):
#        super().__init__(species)

 #       self.attribute = 'vegies'

#    def soup(self):
 #       print("supa de spanac")



#class Verdeturi(Spanac):
#    bark = True

#    def __init__(self, species):
#        super().__init__(species)

 #       self.attribute = 'wild'

 #   def has_more_green(self):
  #      print('adaugam verdeturi')
class Fridge:
    def __init__(self,list_of_my_foods= []):
        for i in list_of_my_foods:
            i=self.foods
    def get_food(self,veggie,meat,milk):
        self.veggie= veggie('veggetable')
        self.meat= meat('type of meat')
        self.milk= milk('type of milk:almond,cashew, coconut')
        meal= Fridge([veggie, meat, milk])
        return meal



class Mealprep:#
    def __init__(self,ingredients = []):
        self.ingredients = ingredients


    def meal_time(self):
        if len (self.ingredients) !=0:
            self.meal_time = max ([i.ingredients for i in self.ingredients if i)]

class Difficulty:
    pass
class MealChanger: #for me to change the meal if i don't like it
    pass
