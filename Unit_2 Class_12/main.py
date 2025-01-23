# import module
# print(module.add_task(5))

for i in range(5):
    if i == 3:
        # continue
        break
    print(i) # this line will skip



# import my_func
# user_input = input()

# print(my_func.greet(user_input)) # module_name.func_name()
# print(my_func.good_morning())
# print(my_func.good_night())

from my_func import greet, good_morning, good_night

print(greet("Nilim"))

print(good_morning())

print(good_night())