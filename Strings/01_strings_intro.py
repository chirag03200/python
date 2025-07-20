name = "harry"  #hum isme kuch bhi change nhi kr skte  na r ko p bna skte h na kuch or

nameshort = name[0:3] #print aayega  har index 0 to 2

print(nameshort)

character1 = name[1]
character0 = name[0]
 
print(character1) # index 1 print ho jaayega 'a'
print(character0) # index 1 print ho jaayega 'h'
 

# negative indexing
print(name[-4:-1]) # print arr
print(name[1:4]) # print arr

character = name[-3] # ye r print krega because negative indexing piche se hoti h
print(character) # index 1 print ho jaayega 'r'

print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])