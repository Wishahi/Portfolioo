# from json import load
from MenuItem import menuItem

def show_user_menu(self):
        user = input
        ('''(a) Add an item to menu
            (d) Delete item from menu
            (v) View the menu
            (x) Exit Menu ''' )

        if user == 'a':
            add_item_to_menu() 
        if user =='d':
            remove_item_from_menu()
        if user == 'v':
                pass
        if user == 'x':
            return 'Exit'



def add_item_to_menu(self):
    name = input("Please input a items name")
    price = int(input("Please input items price"))
    newItem = menuItem(name, price)
    newItem.save()

def remove_item_from_menu():
    removeItemm = input ("Please input item you would like to remove")
    newItem = menuItem(removeItemm)
    newItem.delete()

def show_restaurant_menu():
    menuItem.all()
        


# menu = add_item_to_menu()
# menu("Chips", 20)
# show_user_menu()
# remove_item_from_menu()
