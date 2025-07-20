# Append se hum lsit me element ko add kr skte h
# sort se sorting kr skte h list ko
# reverse bhi kr skte h
# pop bhi kr skte h mtlb delete kr skta h
# insert kr skte h (1,3) 1st index pr 3rd value insert kr skte h
# Extend function ka use kr skte h hum for adding two list
# We use 'Copy' function to copy the same value of one list to another


friends = ["Apple","orange",5,453,56,False,"chirag","Rahul"]

del friends[0]
print(friends) # Apple will be delete

friends.clear()
print(friends)

friends.append("GULAB") # apppend se gulab will be add in list
print(friends)

l1  = [1,2,4,2,6,32,2,7,8,5]

l1.sort()
print(l1)

# l1.reverse()
# print(l1)

l1.insert(5,34) # 5ve index pr 34 insert kro
print(l1)

l1.pop(3) # index 3 ki value pop means delete ho jaayegi
print(l1)

print(l1.pop(3)) # ye vo value print krega jo delete ho gyi 

l1.remove(3)
print(l1)

print(l1.index(1)) # ye print krega ki 1 konse index pr h
print(l1.index(2)) # ye print krega ki 2 konse index pr h
print(l1.index(5)) # ye print krega ki 5 konse index pr h

print(l1.count(2)) # ye count krega ki 2 kitni baar aaya h

l2 = l1
l2[0] = 0
print(l1) # l1 ka index 0 change ho jaayega phke 1 tha now 0
print(l2)

# If we want ki orignal list me change nhi ho to we use copy function
l2 = l1.copy()
l2[0] = 0
print(l1)  # ye purani vaali hi aayegi
print(l2)  # isme l1 ki saari values copy ho jaayegi or idka 0 index 1 se 0 ho jaayeag

m = [84,888,900]
n = [55,65,32]
l1.extend(m)
l1.extend(n)
print(l1) # yha m or n ki values l1 me store ho jaayegi

# adding of two list

k = l1 + m + n
print(k) # yha teeno list add ho jaayegi

print(l1) # yha purani list hi use hogi

#Looping 

for fruit in friends:
    print(fruit)

for i in range(len(friends)):
    print(i,friends[i]) # it's give me no. of index with elements (index+value)

# insetead of range(len) we use enumerate function

for i, friend in enumerate(friends):
    print(i,friend) 


i=0
while i<len(friends):
    print(friends[i])
    i+=1
