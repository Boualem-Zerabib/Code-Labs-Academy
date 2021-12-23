def reverse(string):
    string = string[::-1]
    return string
  
s = input("Please enter your string here: ")
s = str(s)

print ("The original string  is : ",s)
  
print ("The reversed string is : ",reverse(s))
