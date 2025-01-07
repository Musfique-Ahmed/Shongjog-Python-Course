# Write a program to check if a number is even or odd and also if it is divisible by 5.

# Input: Number from user
number = 25#int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0: # even
    print(f"{number} is an even number.")
    # Nested condition to check if the number is divisible by 5
    if number % 5 == 0:
        print(f"{number} is also divisible by 5.")
    else:
        print(f"{number} is not divisible by 5.")
else: # odd
    print(f"{number} is an odd number.")
    # Nested condition to check if the number is divisible by 5
    if number % 5 == 0:
        print(f"{number} is divisible by 5.")
    else:
        print(f"{number} is not divisible by 5.")
