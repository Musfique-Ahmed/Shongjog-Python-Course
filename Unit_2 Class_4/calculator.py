# 1. num-1, 2. num-2, 3. operation?

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num_1 + num_2
elif operation == "-":
    result = num_1 - num_2
elif operation == "*":
    result = num_1 * num_2
else:
    result = num_1 / num_2

print(f"The result of {num_1} {operation} {num_2} is: {result}")


x = 4

print(x ** .5)
