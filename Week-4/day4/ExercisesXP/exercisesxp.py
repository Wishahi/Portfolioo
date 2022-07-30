from dis import dis


# #Exercise 1
# def display_message():
#     print("I am learning Python for the next two months")


# display_message()   



#Exercise 2
# def favorite_book(title):
#     print("One of my favorite books is " + title)

# favorite_book("Alice in Wonderland")  



#Exercise 3
# def describe_city(city, country="UK"):
#     print(city + " is in " + country)

# describe_city("Paris", "France")
# describe_city("London")


#Exercise 4




#Exercise 5
# def make_shirt(size='L', text=' I love Python'):
#     print("The size of the shirt is " + size + " and the text is" + text)


# make_shirt()
# make_shirt(size='M')
# make_shirt(size='XXL', text="how you doing")
# make_shirt(size='S', text="Cei la Vie")


#Exercise 6
# magicians = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# def show_magicians(magicians):
#      for magician in magicians:
#         print(magician)

# # show_magicians(magicians)

# def make_great(magicians):

#  great_peoples = []

#  while magicians:
#     magician = magicians.pop()
#     great_people = magician + ' The Great'
#     great_peoples.append(great_people)



#  for great_people in great_peoples:
#      magicians.append(great_people)

# make_great(magicians)  
# show_magicians(magicians)


#Exercise 7
import random
def get_random_temp():

 x = random.randint(-10,40)
 


 print(x)               

get_random_temp()

def main():

 current_temp = get_random_temp
#  print("The current temperate is " + str(current_temp) + " degrees Celcius")

    
 if current_temp < 0:
    print("Brrr, that’s freezing! Wear some extra layers today")
 elif current_temp == 0 & current_temp <=16:
    print("Quite chilly! Don’t forget your coat")  
 elif current_temp == 16 & current_temp <=23:
    print(" It's getting warmer")  
 elif current_temp == 24 & current_temp <=32:
    print("Finally getting warm!")  
 elif current_temp == 32 & current_temp <=40:
    print("Make sure you stay deyhdrated")   


main()
