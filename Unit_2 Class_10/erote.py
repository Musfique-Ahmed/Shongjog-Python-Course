# OverWrite
with open("C:/Musfique's Folder/Python/Shongjog-Python-Course/Unit_2 Class_10/my_info.txt", "w") as file:
    file.write("Hello World! \n")

    file.close()

# Add 
with open("C:/Musfique's Folder/Python/Shongjog-Python-Course/Unit_2 Class_10/my_info.txt", "a") as file:
    file.write("My name is Musfique Ahmed!")
    file.close()




def printing_name(name):
    print(f"MYT name is {name}")