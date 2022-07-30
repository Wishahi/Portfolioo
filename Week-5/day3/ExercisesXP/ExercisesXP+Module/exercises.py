# #Exercise 2
# from random import *
# s = int(input("Enter random number ::"))
# x = randint(1, 100)   
# 5
# if s == x:
#     print("We have matching numbers, Hooray!")

#Exercise 3
# import string
# import random
 
# N = 5
# res = ''.join(random.choices(string.ascii_letters, k=N))
# print("The generated random string : " + str(res))


#Exercise 4

# import datetime

# today_date = datetime.date.today()
# print(f"Today is the {today_date.day}/{today_date.month}/{today_date.year}")

#Exercise 5
# from datetime import date
# import datetime
# today_date = datetime.date.today()
# jan_date = date(2023, 1, 1)
# delta = today_date - jan_date
# print(delta.days)

#Exercise 6 help
# from datetime import date
# import datetime
# def get_user_birthday():
#     year = int(input('When is your birthday? [YY] '))
#     month = int(input('When is your birthday? [MM] '))
#     day = int(input('When is your birthday? [DD] '))

#     birthday = datetime.datetime(year,month,day)
   
#     today = datetime. datetime. now()
#     difference = (today - birthday)
#     minutes = int(difference. total_seconds() / 60)
#     print(minutes)


#Exercise 7
# from datetime import date
# import datetime

# def numOfDays(date1, date2):
#     return (date2-date1).days

# date1 = today_date = datetime.date.today()
# date2 = date(2022, 12, 25)
# print(numOfDays(date1, date2), "days")

#Exercise 8 help

#Exercise 9 help

