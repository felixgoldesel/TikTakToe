import numpy as np

print("Wo willst du ein Zeichen setzen? ")

input_field = int(input())

a = '|   |'
b = '|   |'
c = '|   |'

list = []
rows = 3
columns = 3

for i in range(rows):
    column = []
    for j in range(columns):
        column.append(' ')
    list.append(column)
#print(list)


arr = np.array(list)
#arr[2, 1] = 'X'
#print(arr)

if input_field <= 3:
    if input_field == 1:
        arr[0, 0] = 'X'
    if input_field == 2:
        arr[0, 1] = 'X'
    if input_field == 3:
        arr[0, 2] = 'X'



print('-----')
print(arr)
print('-----')




