salary_info = {}

while True:
    user_name = input("Please enter your name: (Enter 'quit' to exit)")
    if user_name == "quit":
        break
    else:
        salary = int(input("Enter your salary: "))
        
        salary_info[user_name] = salary

        print("Your info was added to the dictionary!!!")

print(salary_info)

