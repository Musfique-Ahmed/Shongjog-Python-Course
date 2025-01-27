class Account:
    def __init__(self, name, ac_no, balance = 500):
        self.name = name
        self.ac_no = ac_no
        self.__balance = balance

    def show_balance(self):
        print(self.__balance)


ac_1 = Account("Musfique", 23470, 10000)
print(ac_1.name)
print(ac_1.ac_no)
# print(ac_1.__balance)
ac_1.show_balance()