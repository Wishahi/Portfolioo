#Challenge 1
# name = input("Enter a word: ")

# dct=dict()
# for i in range(len(name)):
#     dct[i]=name[i]
# print(dct)

#OR
# foo = {x : [] for x in name}   
# for i,x in enumerate(name):
#     foo[x].append(i) 
#     print(foo)

#Challenge 2
canBuy= []
items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"

# for key,value in items_purchase.items():
#     if value < '$300':
#         print("K:", (key))

# for sub in items_purchase:
#     for key in sub:
#         sub[key] = int(sub[key])
#         print(sub)

dict_with_ints = {k:int(v.strip("$").replace(",","")) for k, v in items_purchase.items()}
print(dict_with_ints)
