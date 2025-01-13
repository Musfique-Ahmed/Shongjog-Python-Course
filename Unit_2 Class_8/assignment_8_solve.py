# Task 1: Print Numbers from 1 to 10
print("Task 1: Print Numbers from 1 to 10")
i = 1
while i <= 10:
    print(i, end=', ' if i < 10 else '\n')
    i += 1
print()

# Task 2: Sum of Natural Numbers
print("Task 2: Sum of Natural Numbers")
n = 20
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print(f"Sum of numbers from 1 to {n} is {total}")
print()

# Task 3: Guess the Number Game
print("Task 3: Guess the Number Game")
correct_number = 7
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == correct_number:
        print("Correct!")
        break
    else:
        print("Wrong, try again!")
print()

# Task 4: Count Digits in a Number
print("Task 4: Count Digits in a Number")
number = 12345
count = 0
while number > 0:
    number //= 10
    count += 1
print(f"Number of digits: {count}")
print()

# Task 5: Print Multiples of 3
print("Task 5: Print Multiples of 3")
i = 3
while i < 30:
    print(i, end=', ' if i < 27 else '\n')
    i += 3
print()

# Task 6: Reverse a Number
print("Task 6: Reverse a Number")
number = 1234
reverse = 0
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10
print(f"Reversed number: {reverse}")
print()

# Task 7: Remove All Items from a List
print("Task 7: Remove All Items from a List")
fruits = ['apple', 'banana', 'cherry']
while fruits:
    print(fruits)
    fruits.pop(0)
print(fruits)  # Prints the empty list
print()

# Task 8: Fibonacci Series
print("Task 8: Fibonacci Series")
n = 50
a, b = 0, 1
while a <= n:
    print(a, end=', ' if a + b <= n else '\n')
    a, b = b, a + b
print()

# Task 9: Keep Doubling Until Exceeding 1000
print("Task 9: Keep Doubling Until Exceeding 1000")
x = 1
while x <= 1000:
    print(x, end=', ' if x * 2 <= 1000 else '\n')
    x *= 2
print()

# Task 10: Nested While Loops - Print a Pattern
print("Task 10: Nested While Loops - Print a Pattern")
rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print(j, end=' ')
        j += 1
    print()
    i += 1
