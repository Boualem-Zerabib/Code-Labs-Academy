l = []
print("All of the even numbers that are between 1 and 299 are in the following list:")
for f in range(1,300):
   if(f % 2 == 0):
    l.append(f)
print(l)    

print("-the length of my list is :" , len(l))
for k in l:
   print("the square of", k ,"is :", k**2 )
