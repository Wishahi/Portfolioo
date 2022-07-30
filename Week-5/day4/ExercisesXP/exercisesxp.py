# import json
# import random
# def get_words_from_file():

#     with open(r'C:\Users\Leen Wishahi\Desktop\DI-Bootcamp-Stage1\Week-5\day4\ExercisesXP\sowpods.txt') as f:
#         contents = f.read()
#         print(contents)
#         wordlist = [contents]


# def get_random_sentence(length):
#     with open(r'C:\Users\Leen Wishahi\Desktop\DI-Bootcamp-Stage1\Week-5\day4\ExercisesXP\sowpods.txt') as f:
#         contents = f.readlines()
#         randomwords=random.choices(contents, k =length)
#         print(randomwords)

# def main():        

#     print ('The class generates random words')
#     user = int(input('Input a number between 2 and 20 '))
    
#     if 2 >= user <= 20:
#         file = get_words_from_file()
#         # print(file)
#         print(get_random_sentence(file,user))
        
#     else:
#         return ValueError    


        
# get_random_sentence(5)
# # get_words_from_file()
# main()


# #Exercise 2
# # import json
# # sampleJson = """{ 
# #    "company":{ 
# #       "employee":{ 
# #          "name":"emma",
# #          "payable":{ 
# #             "salary":7000,
# #             "bonus":800
# #          }
# #       }
# #    }
# # }"""
# # aDict = json.loads(sampleJson)
# # print(type(aDict))
# # print (aDict["company"]['employee']['payable']['salary'])
# # birth_date = aDict["company"]['employee']
# # birth_date['Date_of_birth'] = 2022
# # print(birth_date)
# # print (aDict)
# # json_file = "example.json"
# # with open(json_file,'w') as file:
#     # json.dump(aDict,file)

    