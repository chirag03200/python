# list have multiple datatypes together
# tuple not be change but list may be change 
# index start with 0
# negative indexing bhi kr skte h 
# koi value hme pta lgani ho ki vo list me h ya nhi to hum if ke saath 'in' keyword ka use kr skte h



friends = ["Apple", "orange", 5, 453, 56, False, "chirag", "Rahul"] 
print(friends)

print(len(friends)) # length of list

print(friends[0])

friends[0] = "Grapes" # list me change kr skte h but string me nhi
print(friends[0])

print(friends[1:5]) # index 1 se 4 tk print ho jaayega 

print(friends[-4]) 
print(friends[8-4]) # negative indexing or iska answer same hi aayega.. negative indes ka and hum length - negative index krke bhi nikal skte h

# Agar hme pta krna ho ki koi value is list me h ya nhi to hum ese pta krenge:-

if 8 in friends: # yha hum 'in' keyword ka use kr skte h
    print("yes")
else:
    print("no")

if "chirag" in friends: # yha hum 'in' keyword ka use kr skte h or chirag string h to humne string hi daali h if me bhi
    print("yes")
else:
    print("no")

# ye same cheej string me bhi apply kr skte h 
if "chi" in "chirag":
    print("yes")
else:
    print("no")

if "chia" in "chirag":
    print("yes")
else:
    print("no")

print(friends[:]) # puri list print ho jaayegi
print(friends[1:6]) 

# Jump index
print(friends[1:6:2]) # phle [1:6] print hoga fir 1st value aayegi [1:6] ki or fir jump hoga or 2nd index print hoga
print(friends[1:6:3]) # phle [1:6] print hoga fir 1st value aayegi [1:6] ki or fir jump hoga or 3rd index print hoga
