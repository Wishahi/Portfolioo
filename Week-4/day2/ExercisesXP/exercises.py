# #Exercise 1 -- ask about removing
# my_fav_numbers = {1,3,5,7,9,11,12}
# my_fav_numbers.add(99)
# my_fav_numbers.add(100)
# # my_fav_numbers.pop()
# # del my_fav_numbers[-1]
# # my_fav_numbers[:-1]
# friend_fav_numbers = {200,300,400,500}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)


#Exercise 2
#The answer is no. Tuples are immutable, and therefore cannot be updated

#Exercise 3
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.append("Apples")
# basket_count = basket.count("Apples")
# # basket.clear()
# print(basket)
# print(basket_count)

#Exercise 4
#1: A integer is  whole number, while a float is a point number
#2: By using the round function
#3
# a_list = list(range(1, 5))

# print(a_list)
# [1,2,3,4,5]
# step = 2
# vec = [1,2,3,4,5]
# vec2 = [i/step for i in range(len(vec))]
# print(vec2)

#Exercise 5
# for i in range(1, 21):
#     if i % 2 ==0:
#         print(i)

#Exercise 6
# name = "Leen"
# while True:
#   user = input('Input your name: ')
#   if (user) == name:
#     print('Congrats! You win!')
#     break
#   else:
#     print('Wrong guess...')

#Exercise 8
# price = 10
# toppings = input("Enter a series of pizza toppings ").split(",")
# for topping in toppings:
#     print(f"I will add {topping} to the pizza")
#     price +=2.5
# print(price)
# print(" ".join(toppings))



#Exercise 9
# import numbers
# tickets = int(input("How many tickets is needed "))
 
# for i in range(tickets):
#     age = int(input("How old are you?"))
#     if age < 3:
#         price1 = 0
#         print(price1)
#     elif age > 3 and age <=12:
#         price2= 10
#         print(price2)
#     else:
#         price3= 15
#         print(price3) 




#Exercise 10 and Exercise 11
# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
# finished_sandwiches = []

# print("I'm sorry, we're all out of pastrami today.")
# while 'Pastrami sandwich' in sandwich_orders:
#     sandwich_orders.remove('Pastrami sandwich')

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
    
#     finished_sandwiches.append(current_sandwich)

# for sandwich in finished_sandwiches:
#     print(" I made your " + sandwich)




         

