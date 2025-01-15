def add(*args): # args = (1,4,5,6) makes a tuple
    # print(args)
    return sum(args)
print(add(1,4,5,6))

def print_info(**kwargs): #kwargs = {'name': 'Anik', 'age': 24} makes a dictionary
    # print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_info(name = "Anik", age = 24,gender = "Male")