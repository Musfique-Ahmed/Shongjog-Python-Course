class Person: #Parent class
    def __init__(self, name, blood_grp, age):
        self.name = name  
        self.blood_grp = blood_grp
        self.age = age
          
    def display_info(self):
        print(f'''
Name: {self.name}
Age: {self.age}
Blood Group: {self.blood_grp}
                ''')
    
    def donate_blood(self, last_dnation_date):
        if last_dnation_date < 4:
            print(f"You are not eligible for donating blood.")
        else:
            print(f"You are eligible for donating blood.")


class Student(Person): # child class
    def __init__(self, name, blood_grp, age, id, section, grade):
        super().__init__(name, blood_grp, age)
        self.id = id
        self.section = section
        self.__grade = grade

    def display_info(self):
        print(f'''
Name: {self.name}
ID: {self.id}
Section: {self.section}
                ''')
        
    def get_grade(self):
        print(f"{self.name}'s grade is: {self.__grade}")


s_1 = Student("Manha","O-",15, "2750136768", "A", "A+")
s_1.display_info()
s_1.get_grade()
s_1.donate_blood(3)
