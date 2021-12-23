
def Numberisprime(s):
    if (s==1):
        return False
    if (s==2):
        return True
    else:
        for k in range(2,s):
            if(s % k == 0):
                return False
        return True 

b = input()
b = int(b)
if(Numberisprime(b)):
    print(b,"is prime")
else:
    print(b,"is not prime")
