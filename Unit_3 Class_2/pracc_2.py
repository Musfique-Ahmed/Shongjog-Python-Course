def log_message(func):
    def wrapper(*args, **kwargs):
        print("Logging: Displaying employee details.")
        return func(*args, **kwargs)
    return wrapper

class Employee:
    employee_list = []

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        Employee.employee_list.append(self)

    def display_details(self):
        pass

    def increase_salary(self, increment):
        self.salary += increment

    @classmethod
    def total_salary(cls):
        total_slary = 0
        for employee in cls.employee_list:
            total_slary += employee.salary 

        return total_slary
    
    @log_message
    def display_details(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}")



