l = [i for i in range(10)]
print(l) # print 0 to 9 number

l = [i*i for i in range(10)]
print(l) # print square of 0 to 9 number

l = [i*i for i in range(10)  if i%2==0]
print(l) # print square of 0 to 9 but only even no

l = [i for i in range(10) if i%2==0]
print(l) # print 0 to 9 number but only even