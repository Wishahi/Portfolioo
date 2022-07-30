
# matrix = [
#     ['7','i','3'],
#     ['T', 's', 'i'],
#     ['h', '%', 'x'],
#     ['i', '', '#'],
#     ['s', 'M'],
#     ['$', 'a'],
#     ['#', 't', '%'],
#     ['^', 'r', '!']
# ]

# for elem in zip(*matrix):
#     print(''.join(elem))


# def get_col(matrix, i):
#     return [row[i] for row in matrix]


# get_col()    
import re
n,m =map(int,(input().split()))
a,b = [],""
for _ in range(n):
    a.append(input())
    
for z in zip(*a):
    b +="".join(z)

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)"," ",b))