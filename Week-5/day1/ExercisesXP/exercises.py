#Exercise 1
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
        

# cat1 = Cat("Koko", 1)
# cat2 = Cat("Fufu", 3)
# cat3 = Cat("Minni", 5)        


# def oldestCat(c1, c2, c3):
#     catsname= [c1.name, c2.name, c3.name]
#     catsage = [c1.age, c2.age, c3.age]
#     return max(catsname,catsage)

# print(f"The oldest cat is {oldestCat(cat1, cat2, cat3)} and is {oldestCat(cat1, cat2, cat3)} years old")  
# 
# work on cats name  


#Exercise 2
# from unicodedata import name


# class Dog():
#     def __init__(self, name, height):
#             self.name = name
#             self.height = height


#     def bark(self):
#         print("{} goes woof".format(self.name))    
        
#     def jump(self):
#         print("{} jumps {} cm high!".format(self.name, self.height))


# new_Dog = Dog("Oscar", 10*2)
# new_Dog.bark()
# new_Dog.jump() 
# davids_dog = Dog("Rex", 50)
# davids_dog.bark()
# davids_dog.jump()
# sarahs_dog= Dog("Teacup", 20)
# sarahs_dog.bark()
# sarahs_dog.jump()

# dogs= [new_Dog.height,davids_dog.height,sarahs_dog.height]

# for i in dogs:
#     if new_Dog.height>davids_dog.height:
#         biggerDog = new_Dog
# print(biggerDog.height)
# print(f'The bigger dog is {new_Dog.name}')


#Exercise 3
# class Song():
#     def __init__(self, lyrics):
#         self.lyrics =list(lyrics)
        

#     def sing_me_a_song(self):
#         for line in self.lyrics:
#          print(line)



# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()

#Exercise 4
from itertools import groupby
class Zoo():
    def __init__(self, zoo_name):
        self.animals= []
        self.name = zoo_name

    def add_animal(self,new_animal):
        if self.name in self.animals:
            print("Sorry already exists")
        else:    
           self.animals.append(new_animal)

        
    def get_animals(self):
        print('\n'.join(map(str, self.animals))) 
    
    def sell_animal(self,animal_sold):
        if self.name in self.animals:
            print("Sorry animal doesnt exists")
        else:    
           self.animals.remove(animal_sold)

    def sort_animals(self):
     util_func = lambda x: x[0]
     temp = sorted(self.animals, key = util_func)
     hello = [list(ele) for i, ele in groupby(temp, util_func)] 



     print("List of categories: " + str(hello))

     #ask about number 7 


ramat_gan_zoo = Zoo("Batata")
ramat_gan_zoo.add_animal("Giraffe")
ramat_gan_zoo.add_animal("Zebra")
ramat_gan_zoo.add_animal("Lion")
ramat_gan_zoo.add_animal("Lioness")
ramat_gan_zoo.add_animal("Bear")
ramat_gan_zoo.add_animal("Goose")
ramat_gan_zoo.get_animals()
ramat_gan_zoo.sell_animal("Bear")
# ramat_gan_zoo.sell_animal("Dog")
ramat_gan_zoo.sort_animals()    

        


    