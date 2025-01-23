# file = open("C:/Musfique's Folder/Python/Shongjog-Python-Course/Unit_2 Class_10/my_info.txt", "r")

# # content = file.read()
# content = file.readlines() #Output: ['I am Musfique Ahmed.\n', '\n', 'Who are you?\n', 'sgjhdkgh']
# # content = file.readline()
# lines = ""

# for line in content:
# # print(content)
#     lines += line.strip()
#     print(line)
# print(lines)

# file.close()


# file = open("my info.txt" , "r")
# content = file.read()
# print(content)
# file.close()



# # Traceback (most recent call last):
# #   File "d:\Ahnaf Doc\Python H_W\unit_2_class_10\file.py", line 1, in <module>
# #     file = open("info.txt", "r")
# #            ^^^^^^^^^^^^^^^^^^^^^
# # FileNotFoundError: [Errno 2] No such file or directory: 'info.txt'



# file = open("C:/Musfique's Folder/Python/Shongjog-Python-Course/Unit_2 Class_10/my_info.txt", "r")

# content = file.readlines() 
# lines = ""

# for line in content:
#     lines = lines + line.strip() + " " # \n kete dise

# print(lines)

# file.close()


# # file = open("C:/Musfique's Folder/Python/Shongjog-Python-Course/Unit_2 Class_10/my_info.txt", "r")

# # content = file.readline()
# # print(content)

# # file.close()

# # from erote import printing_name
# import erote

# erote.printing_name("Musfique")


file = open("my_info_2.txt", "r")

content = file.read()

# content = file.readlines()
# print(file.readline())
# print(file.readline())
# print(file.readline())
print(content)

# for line in content:
#     print(line)

file.close()



# file = open("my_info.txt", "w")

# file.write("I am Sajid.")

# file.close()


# file = open("my_info.txt", "a")

# file.write("I am Sajid.")

# file.close()