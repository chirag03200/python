matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][0])
print(matrix[1][2])

# Loop through nested list

for row in matrix:
    for item in row:
        print(item)
        print(item,end='')



num = [10, 20, 30, 40, 50, 60]

print(len(num)) # lenght of list
print(sum(num)) # sum of list
print(min(num)) # mininmum in the list
print(max(num)) # maximum in the list

# Conversion other types into list
chars = list("chirag")
print(chars) # print chirag as a list
print(len(chars)) # chirag have 6 letters so the length of list is 6

tup = (1,2,3,4)
print(list(tup))