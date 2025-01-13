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

data_base = {}

while True:
    user_name = input("Enter Your name (Enter 'quit' to exit): ")
    if user_name == "quit":
        break
    else:
       
        age = int(input("Enter your age: "))
        sch = input("Enter your school name: ")

        lst = [age, sch]

        data_base[user_name] = lst

        print(f"Your registered data base are mentioned below")

print(data_base)