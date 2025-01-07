import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def exponent(a, b):
    return a ** b

def logarithm(a, b):
    return math.log(b, a)

def sine(a):
    return math.sin(a)

def cosine(a):
    return math.cos(a)

def tangent(a):
    return math.tan(a)

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponent")
print("6. Logarithm")
print("7. Sine")
print("8. Cosine")
print("9. Tangent")

choice = int(input("Enter choice(1/2/3/4/5/6/7/8/9): "))

if choice == 5 or choice == 6:
    num1 = float(input("Enter base: "))
    num2 = float(input("Enter value: "))
elif choice >= 7 and choice <= 9:
    num1 = float(input("Enter angle in radians: "))
else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

if choice == 1:
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == 4:
    print(num1, "/", num2, "=", divide(num1, num2))

elif choice == 5:
    print(num1, "^", num2, "=", exponent(num1, num2))

elif choice == 6:
    print("log", num1, "of", num2, "=", logarithm(num1, num2))

elif choice == 7:
    print("sin(", num1, ") =", sine(num1))

elif choice == 8:
    print("cos(", num1, ") =", cosine(num1))

elif choice == 9:
    print("tan(", num1, ") =", tangent(num1))
else:
    print("Invalid Input")