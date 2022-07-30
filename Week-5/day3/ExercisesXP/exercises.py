#Exercise 1
# def abs():
#     '''Return the absolute value of 
#         the argument.'''
   
#     return None
  
# print("Using __doc__:")
# print(abs.__doc__)
  
# def int():
#     '''Returns an integer value, which is
#      equivalent of binary string in the given base.'''
   
#     return None
  
# print("Using __doc__:")
# print(int.__doc__)

# def input():
#     ''' returns a string object. Even if the inputted value 
#     is an integer it converts it into a string.'''
   
#     return None
  
# print("Using __doc__:")
# print(input.__doc__)

#Exercise 2
from locale import currency
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        print("{} {}".format(str(self.amount),self.currency))  
        # return  'salary=$'+str(self.amount) + 'name='+self.currency
        return f'{self.amount} {self.currency}'

    def __int__(self):
        print("{}".format(self.amount))
        return f'{self.amount} {self.currency}'

    def __repr__(self):
        # print("{} {}".format(str(self.amount),self.currency))  
        return f'{self.amount} {self.currency}'   

    # def __add__(self, otherAmount):
    #     return Currency(self.amount + otherAmount.amount)
        


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
str(c1)        
int(c1)
repr(c1)


# c1_Int = int(c1.amount)
# print (c1_Int)
# repr = c1.__repr__()
# print (repr)
# print(c1_Int+5)
# c2 = int(c2.amount)
# print (c1_Int+c2)

# print (f'{c1_Int} {c1.currency}')
# c1_Int+=5
# print (f'{c1_Int} {c1.currency}')
# c1_Int +=c2
# print(f'{c1_Int} {c1.currency}')

if c1.currency + c3.currency :
    raise ValueError(f"Cannot add between Currency type {c1.currency} and {c3.currency}")
print (c1.currency + c3.currency)