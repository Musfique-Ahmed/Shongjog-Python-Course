my_info = {
    'Name': 'Musfique', 
    'Age': 24, 
    'blood group': 'A+', 
    'Grade': 'A+', 
    'Gender': 'Male'
    }

# Accessing all keys in the dictionary
# 1. 
for key in my_info: # for key in dict_name:
    print(key)
# 2.
for key in my_info.keys(): #  for key in dict_name.keys():
    print(key)

# Accessing all vlaues
for value in my_info.values(): # for value in dict_name.values():
    print(value)

# Accessing key and value
for key, anik in my_info.items(): # for key, value in dict_name.items():
    print(f"{key} : {anik}")

# Practice Problem:
# Write a program to loop through a dictionary of student names and 
# their marks, printing each name and mark.


my_dict={
    "MANHA":"1000", 
     "RAMISA":"800", 
    "ARIFA":"600", 
    "REHAN":"400"}
print(my_dict)
for key in my_dict:
    print(key)
for value in my_dict.values():
    print(value)
for key,value in my_dict.items():
    print(f"{key}:{value}")