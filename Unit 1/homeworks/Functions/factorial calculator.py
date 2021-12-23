def Factorial(k):
    if (k==0 or k==1):
        return 1
    else:
        return k * Factorial(k-1)   
k = input("please enter your number: ")
k = int(k)

print("the factorial of",k,"is:",Factorial(k) )