# Bank Account
class CustomError(Exception):
    """Exception raised for custom error scenarios."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return f"{self.message}"
    
class BankAccount:
    def __init__(self, name, ac_no, balance = 500):
        self.name = name
        self.ac_no = ac_no
        self.__balance = balance # Private variale

    def show_balance(self): #getter method
        print(f"Balance: {self.__balance}")

    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount}BDT was deposited to your account!")

    def withdraw(self, amount):
        
        if (self.__balance - amount) < 500:
            raise CustomError("You cannot withdraw this amount, You don't have enough Money!")
        else:
            self.__balance -= amount
            print(f"{amount} BDT was withdrawed from your account")



ac_1 = BankAccount("Musfique", 23470, 10000)
# print(ac_1.balance)
print(ac_1.name)
print(ac_1.ac_no)
# print(ac_1.__balance)
ac_1.show_balance()
# ac_1.balance = 50000
# print(ac_1.balance)
ac_1.deposit(5000)
ac_1.show_balance()
ac_1.withdraw(14000)
ac_1.show_balance()
ac_1.withdraw(600)
ac_1.show_balance()
"""
Create a "Student" class with a private variable __grade. 
Add a method get_grade() to return the grade safely.
"""



# # Musyab Iqbal
# # 7:01 PM
# class Student:
#     def __init__(self, grade):
#         self.__grade = grade
#     def get_grade(self):
#         return self.__grade  # Getter method to return the grade safely

# student = Student("A")
# print(student.get_grade())  # Output: A
# # AHAN Mahmud Towseem N
# # 7:04 PM
# class Student:
#     def __init__(self, grade):
#         self.__grade = grade

#     def get_grade(self):
#         return self.__grade

# student = Student(69)
# # print(student.__grade)
# print(student.get_grade())  # Output: 69

# # Md Mohiuddin
# # 7:04 PM
# class Student:
#     def __init__(self, grade):
#         self.__grade = grade
        
#     def get_grade(self):
#         return self.__grade  

# student = Student("A+")
# print(student.get_grade())

# # Farzia Lopa
# # 7:07 PM
# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.set_grade(grade)

#     def set_grade(self, grade):
#         if 0 <= grade <= 100: self.__grade = grade
#         else: raise ValueError("Invalid grade")

#     def __str__(self):
#         return f"{self.name} - {self.__grade}, Passed: {'Yes' if self.__grade >= 60 else 'No'}"

# # Example usage:
# student = Student("Manha Binta Bellah", 85)
# print(student)  # Alice - 85, Passed: Yes

# class Student:
#     def __init__(self, name, id, section, grade):
#         self.name = name
#         self.id = id
#         self.section = section
#         self.__grade = grade

#     def display_info(self):
#         print(f'''
# Name: {self.name}
# ID: {self.id}
# Section: {self.section}
#                 ''')
        
#     def get_grade(self):
#         print(f"{self.name}'s grade is: {self.__grade}")


# s_1 = Student("Manha", "2750136768", "A", "A+")
# s_1.display_info()
# s_1.get_grade()


        

# class Student:
#     def __init__(self,grade):
#         self._grade = grade
#     def show_grade(self):
#         return self._grade
# stu_1 = Student("A")
# print(stu_1.show_grade())