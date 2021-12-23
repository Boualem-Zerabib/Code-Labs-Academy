def InRange(k):
    if k in range(n,m):
        return True
    else:
        return False

k = input("Please input your number here: ")
n = input("Please input the boundaries of the range (min first , max second): ")
m = input()

k = int(k)
n = int(n)
m = int(m)

if(InRange(k)):
    print("the number is in the range.")
else:
    print("the number is not in the range.")