#Exercise 1
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())



# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'



# all_cats= [Bengal("Koko", "5"), Chartreux("Bata", "12"), Siamese("Leen", "20")]

# sara_pets = Pets(all_cats)
# sara_pets.walk()


#Exercise 2
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight


    def bark(self):
     str1 = "{} is barking".format(self.name)
     return str1

    def run_speed(self):
        speed = (self.weight/self.age*10)
        return speed

    def fight(self,other_dog):
        # winner = max(self.run_speed * self.weight
        # return winner 
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            print ("{} won".format(self.name))
        else:
            print ("{} won".format(self.name)) 
    



# dog1 = Dog("Oscar", 2, 23)
# dog2 = Dog("Rex", 4, 15)
# dog3 = Dog("Minnie", 5, 5)
# dog1.bark()
# dog1.run_speed()
# dog1.fight(dog2)

# dog2.bark()
# dog2.run_speed()
# dog2.fight(dog3)

# dog3.bark()
# dog3.run_speed()
# dog3.fight(dog1)


        
