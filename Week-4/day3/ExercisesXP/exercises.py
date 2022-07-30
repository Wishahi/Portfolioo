#Exercise 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# dictionary = dict(zip(keys,values))
# print(dictionary)

#Exercise 2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# for key, value in family.items():
#     if value < 3:
#         price1 = 0
#         print(price1)
#     elif value > 3 and value <=12:
#         price2= 10
#         print(price2)
#     else:
#         price3= 15
#         print(price3)

#     print("K and V:", (key,value))


#BONUS
# family = []

# while True:

#     name = input("Enter name: ")
#     age = int(input("Enter age: "))

#     new_info = {
#         'name': name,
#         'age': age
#     }

#     family.append(new_info)
     
#     print(family)




#Exercise 3
#2
# brand = {
#     'name': 'Zara',
#     'creation_date':1975,
#     'creator_name': 'Amancio Ortega Gaona',
#     'type_of_clothes': 'men, women, children, home',
#     'international_competitors': 'Gap, H&M, Benetton',
#     'number_stores': 7000,
#     'major_color': {
#         'France': 'blue',
#         'Spain' : 'red',
#         'US' : 'pink, green'
#     }
# }

#3
# brand['number_stores'] = 2

#5
# brand['country_creation'] = 'Spain'
# print(brand)
#6
# if 'international_competitors' in brand:
#     brand['international_competitors'] = 'Gap, H&M, Benetton','Desigual'
#7
# brand_removed = brand.pop('creation_date')
#8
# print(brand['international_competitors'][-1])
# #9
# print(brand['major_color']['US'])
# #10
# print ("Length : %d" % len (brand))
# #11
# print(brand.keys())

#12
# more_on_zara = {
#     'creation_date': 1975,
#     'number_stores': 10000
# }
# #13
# brand.update(more_on_zara)
# print(brand)
# #14
# print(brand['number_stores']) #number has been updated





#Exercise 4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
#1
dict_user = {k: v for v, k in enumerate(users)}
print(dict_user)
#2
print(dict(enumerate(users)))
#3
print(dict(enumerate(sorted(users))))
#4
key1= 'i'
if key1 in users.keys():
    print(users[key1])