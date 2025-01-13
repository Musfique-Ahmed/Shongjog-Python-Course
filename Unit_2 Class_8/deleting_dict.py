my_info = {
    'Name': 'Musfique', 
    'Age': 24, 
    'blood group': 'A+', 
    'Grade': 'A+', 
    'Gender': 'Male'
    }

del my_info['Grade'] # del dict_name["key"]
print(my_info)

poped_value = my_info.pop("Age") # 24
print(poped_value)

print(my_info)

my_info.clear()
print(my_info)


my_books = {
    "Animal Farm": "Charles Dickens", 
    "A Tale Of Two Cities":"Charles Dickes", 
    "Aice in Wondrland":"Lewis Carol"
    }
print(my_books)

my_books["George Orwell"] = "Animal Farm"