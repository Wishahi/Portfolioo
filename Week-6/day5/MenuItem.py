import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Farfoosh12'
DATABASE = 'Restaurant'


def run_query(query):
        """opens connection, runs a query, closes the connection"""
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        try:
            results = cursor.fetchall()
            connection.close()
            return results
        except:
            connection.close()
    
# query = """CREATE TABLE menu_items (
#     id serial PRIMARY KEY,
#     item VARCHAR(100),
#     price INT
#     ); """
        # menuItem("burger", 25)
# run_query(menuItem)   



class menuItem():
    def __init__(self, name, price):
        self.name = name
        self.price = price

        
    def save(self):
        q= f"INSERT INTO menu_items (item, price) VALUES ('{self.name}', '{self.price}') RETURNING id, item, price;"
        return run_query(q)


    def update(self, name, price):
      q = f"UPDATE menu_items SET item = '{name}', price= {price} WHERE item = '{self.name}' OR price = {self.price}"
      return run_query(q)


    def delete(self):
        q=f"DELETE FROM menu_items WHERE item = '{self.name}' OR price = {self.price}"
        return run_query(q)

    def all():
        q=f" SELECT * FROM menu_items"
        return run_query(q)

    def  get_by_name(choice):
        # choice = None
        # while choice == '':
        # choice = input("What Item do you want?")
        q = f"SELECT * FROM menu_items WHERE item = '{choice}'"
        #     # q(choice)
        print (run_query(q)) 
        # return q  

    

# item = menuItem('Veggie Burger', 37)
# item = menuItem('Carrot', 20)
# item.save()
# item.delete()
# item.update('Veggie Burger', 37)
item2 = menuItem.get_by_name('Apple')
# items = menuItem.all()