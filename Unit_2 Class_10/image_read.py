file = open("C:/Musfique's Folder/Python/Shongjog-Python-Course/Unit_2 Class_10/image.png", "rb")

content = file.read()
print(content)

file.close()

file = open("C:/Musfique's Folder/Python/Shongjog-Python-Course/Unit_2 Class_10/image_2.png", "wb")
file.write(content)
file.close()

file = open("C:/Musfique's Folder/Python/Shongjog-Python-Course/Unit_2 Class_10/python-for-beginners-complete-python-programming.jpg", "rb")

content = file.read()
print(content)

file.close()