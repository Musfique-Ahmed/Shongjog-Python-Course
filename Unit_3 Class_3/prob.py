# class Employee:
#     def __init__(self , name , id , salary):
#         self.name = name
#         self.id = id
#         self.salary = salary

#     def promotion(self):
#         increase = 1.10
#         self.salary *= increase
#     def display_info(self):
#         print(f'''
# name: {self.name}
# id: {self.id}
# salary: {self.salary}
#                 ''')
        

# class programmer(Employee):
#     def __init__(self, name , id , salary, language):
#         super()._init_(name , id , salary)
#         self.language = language
#     def get_language(self):
#         print(f"this programmer works in {self.language}")
#     def promotion(self): 
#         increse = 1.30 
#         self.salary *= increse



class Employee:
    def __init__(self,name,id,salary):
        self.name = name
        self.id = id
        self.salary = salary
    def promotion(self):
        increase = 1.10
        self.salary *= increase
    def display_info(self):
        print(f'''
name: {self.name}
id:{self.id}
salary:{self.salary}
                ''')
        
class Programer(Employee):
    def __init__(self, name, id, salary,language):
        super().__init__(name, id, salary)
        self.language = language
    def get_languge(self):
            print(f" THis programmer works in {self.language}")
    def promotion(self): # Method Over riding
        increse = 1.30 # 30% -> 1tk -> 1.30tk
        self.salary *= increse # self.salary = self.salary * increse
e_1 = Employee("Musfique", "9768054", 50000)
e_1.promotion()
e_1.id
e_1 = Employee("Musfique", "9768054", 50000)
e_1.promotion()
e_1.display_info()
p_1 = Programer("Abdullah", "7465223", 10000, "Python")
p_1.promotion()
p_1.display_info()
p_1.get_languge()