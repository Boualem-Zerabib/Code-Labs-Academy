a = 12
s = "hello"
try:
    a + s 
except: 
    a = str(a)
else:
    s = int(s)
finally:
    print(a+s)
