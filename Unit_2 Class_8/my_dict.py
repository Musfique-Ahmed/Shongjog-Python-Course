my_dict = {"Name": "Musfique", "Age": 23, "blood group": "A+", "Grade": None}
print(my_dict)

# lst = [1,2,3]
# print(lst)

# # Accessing the dictionary values
# print(my_dict["Name"])
# print(my_dict["Age"])
# print(my_dict["blood group"])

# add an element
my_dict["Gender"] = "Male"
print(my_dict)
# int, float, string
# update the value of a key
my_dict["Age"] = 24
print(my_dict)
my_dict["Grade"] = "A+"
print(my_dict)
print(my_dict.values())
print(set(my_dict.values()))