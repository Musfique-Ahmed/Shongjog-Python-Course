# Bank Account
class Account:
    def __init__(self, name, ac_no, balance = 500):
        self.name = name
        self.ac_no = ac_no
        self.__balance = balance

    def show_balance(self): #getter method
        print(self.__balance)

    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount}BDT was deposited to your account!")


ac_1 = Account("Musfique", 23470, 10000)
# print(ac_1.balance)
print(ac_1.name)
print(ac_1.ac_no)
# print(ac_1.__balance)
ac_1.show_balance()
# ac_1.balance = 50000
# print(ac_1.balance)
ac_1.deposit(5000)
ac_1.show_balance()

"""
Create a "Student" class with a private variable __grade. 
Add a method get_grade() to return the grade safely.
"""