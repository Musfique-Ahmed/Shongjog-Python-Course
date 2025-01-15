x= 30 # global variavle 
print(x)

def myFunc():
    global x
    x= 2 # global variable
    y = 23 # local variable
    return x


print(myFunc())
print(x)
# print(y)


