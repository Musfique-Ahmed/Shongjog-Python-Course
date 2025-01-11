# while True:
#     customer_input = input("What topings do you want?: ")
#     if customer_input == "quit":
#         break
#     else:
#         print(f"{customer_input} will be added to yout pizza!")


#Movie Tickets: A movie theater charges different ticket prices depending on a person’s age . If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15 . Write a loop in which you ask users their age, and then tell them the cost of their movie ticket 
# while True:
#     age = input("Enter your age (Enter'quit' to stop): ") #type: string

#     if age == "quit":
#         print("Goodbye")
#         break
    
#     age = int(age) # turns anything into integers "34" => 34

#     if age < 3:
#         print("your ticket is free")
#     elif age <= 12:
#         print("your ticket price is 10$")
#     else:
#         print("your ticket price is 15$")


# while True:
#     age = input("Enter you age (Enter 'quit' to stop): ")

#     if age == "quit":
#         print("Goodbye!")
#         break

#     age = int(age)

#     if age<3:
#         print("your ticket is free")
#     elif age<=12:
#         print("your ticket is 10$")
#     else:
#         print("your ticket is 15$")


# while True:
#     customer_input = input("Enter your Age: ")

#     if customer_input == 'quit':
#         break
#     customer_input = int(customer_input)

#     if customer_input < 3:
#         print("The ticket is free")
#     elif customer_input <= 12:
#         print("Your Ticket is 10$")
#     else:
#         print("Your Ticket is 15$")

num = 5

for i in range(num):
    for j in range(i):
        print("*", end="")
    print()