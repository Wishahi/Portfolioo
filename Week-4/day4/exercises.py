# def say_hello(username, language):
#     if language == 'EN':
#         print("Hello " + username)
#     elif language == 'FR':
#         print("Bonjour " + username)
#     else:
#         print("This langauge is not supported: " + language)



# say_hello('Rick', 'FR')   

# def calculation(a, b):
#     return a+b, a-b

# res = calculation(40,10)

# print(res)

def greet_users(users):
    for user in users:
        print("Hello " + user.title() + " !")

usernames = ['steve', 'stan', 'debbie'] 
greet_users(usernames)       