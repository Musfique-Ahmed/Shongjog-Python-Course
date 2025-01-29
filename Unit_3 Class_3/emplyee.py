class Employee:
    def __init__(self, name, id, salary): #parent class
        self.name = name
        self.id = id
        self.salary = salary

    def promotion(self):
        increse = 1.10 #10% -> 1tk -> 1.10tk
        self.salary *= increse # self.salary = self.salary * increse

    def display_info(self):
        print(f'''
Name: {self.name}
ID: {self.id}
Salary: {self.salary}
                ''')


class Programer(Employee): #child class
    def __init__(self, name, id, salary, language):
        super().__init__(name, id, salary) #super init
        self.language = language

    def get_languge(self):
        print(f" THis programmer works in {self.language}")

    def promotion(self): # Method Over riding
        increse = 1.30 # 30% -> 1tk -> 1.30tk
        self.salary *= increse # self.salary = self.salary * increse


e_1 = Employee("Musfique", "9768054", 50000)
e_1.promotion()
e_1.display_info()


p_1 = Programer("Nilim", "8465223", 100000, "Python")
p_1.promotion()
p_1.display_info()
p_1.get_languge()