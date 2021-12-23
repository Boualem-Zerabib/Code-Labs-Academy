def MaxNumberOfTwo(a,b):
    if(a>b):
        return a
    else:
        return b
def MaxNumberOfThree(a,b,c):
    return MaxNumberOfTwo(MaxNumberOfTwo(a,b),c)    

a = input("please input your first number: ")
b = input("please input your second number: ")
c = input("please input your third number: ")
a = int(a)
b = int(b)
c = int(c)

print("The max of the 3 given numbers is: ", MaxNumberOfThree(a,b,c))
