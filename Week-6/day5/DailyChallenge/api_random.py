from cProfile import run
import json
from urllib import request
import psycopg2
import requests
import random


HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Farfoosh12'
DATABASE = 'CountriesAPI'
PORT = 5432

def run_query(query):
        """opens connection, runs a query, closes the connection"""
        try:    
            connection =  psycopg2.connect(host=HOSTNAME,
                    port=PORT,
                    user=USERNAME,
                    password=PASSWORD,
                    database=DATABASE)
            cursor = connection.cursor()
            #first parameter is the query and the second is the values
            cursor.execute(query[0],query[1])
            # cursor.execute(query)
            connection.commit()
            cursor.close()
            connection.close()
        except Exception as ex:
                print(ex)
        finally:
            if connection is not None:
                connection.close()


# query =  '''
#     CREATE TABLE public.country_info (
# 	name varchar NULL,
# 	capital varchar NULL,
# 	flag varchar NULL,
# 	subregion varchar NULL,
# 	population varchar NULL
#     );
#     '''

# run_query(query)  



def getCountries(count):
    # I have changed the url to return only the requested field with no irrelevant data 
    apiCountries = requests.get("https://restcountries.com/v2/all?fields=name,capital,flag,subregion,population")
    loadJson= json.loads(apiCountries.text)
    return random.choices(loadJson, k=10)


def insertToDb(random_countries):
    for dr in random_countries:
        #Some of the countries doesn't have all attributes so we use get instead and give it a default value of not found
        name = dr.get("name","Not Found")
        capital = dr.get("capital","Not Found")
        flag = dr.get("flag","Not Found")
        subregion = dr.get("subregion","Not Found")
        population = dr.get("population","Not Found")
        sql = ('INSERT INTO country_info (name, capital, flag, subregion, population) VALUES(%s,%s,%s,%s,%s)',(name,capital,flag,subregion,population))
        run_query(sql)



if __name__ == "__main__":
    random_countries = getCountries(10)
    insertToDb(random_countries)


# '''
#     CREATE TABLE public.country_info (
# 	name varchar NULL,
# 	capital varchar NULL,
# 	flag varchar NULL,
# 	subregion varchar NULL,
# 	population varchar NULL
#     );
# '''