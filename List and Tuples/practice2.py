# take input of 6 marks with sorted manner

marks =  []

f1 =  int(input("Enter  marks here: "))
marks.append(f1)
f2 =  int(input("Enter  marks here: "))
marks.append(f2)
f3 =  int(input("Enter  marks here: "))
marks.append(f3)
f4 =  int(input("Enter  marks here: "))
marks.append(f4)
f5 =  int(input("Enter  marks here: "))
marks.append(f5)
f6 =  int(input("Enter  marks here: "))
marks.append(f6)
 
marks.sort() # only input denge to ye sort krega(only places ko because of string) phle 2 se start hote h vo likhega fir 3 fir 4 fir so on now we use for sorting int
print(marks)