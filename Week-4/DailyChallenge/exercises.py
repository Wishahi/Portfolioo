import random
user = input("Please write a sentence")
last_char = user[-1]
first_char = user[0]
user_letters = list(user)

if len(user) <10:
    print("string not long enough")
elif len(user) >10:
    print("String too long")
print("First Character is", first_char, 'Last character', last_char)

for i in range(len(user)):
    # str1 = ""
    # str1 +=i

    print(user[:i+1])

random.shuffle(user_letters)
print ("After shuffling: ", user_letters)