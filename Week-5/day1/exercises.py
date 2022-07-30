# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
# p = Point(3,4)

# print("p.x is:", p.x)
# print("p.y:", p.y)

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# first_person = Person("Leen", 24)

# print(first_person.name)
# print(first_person.age)

# class Dog():
#     def __init__(self, name_of_dog):
#         print("His name is" ,name_of_dog)
#         self.name = name_of_dog


#     def bark(self):
#             print("{} barks ! WAF".format(self.name))

#     def walk(self, number_of_meters):
#         print("{} walked {} meters".format(self.name, number_of_meters))        
    
#     def rename(self, new_name):
#         self.name = new_name



# shelter_dog = Dog("Rex")
# # other_shelter_dog = Dog("Jimmy")
# # shelter_dog.bark()
# # shelter_dog.walk(10)
# shelter_dog.rename("Paul")


# class Person():
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def show_details(self):
#     print("Hello my name is " + self.name)

#   def rename(self, new_name):
#     self.name = new_name  

# first_person = Person("John", 36)
# first_person.show_details()
# first_person.rename("Hannah")

# class Computer():

#     def description(self, name):
#         """
#         This is a totally useless function
#         """
#         print("I am a computer, my name is", name)
#         #Analyse the line below
#         print(self)

# mac_computer = Computer()
# mac_computer.brand = "Apple"
# print(mac_computer.brand)

# dell_computer = Computer()

# Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
# dell_computer.description("Mark")


class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)


        
    

