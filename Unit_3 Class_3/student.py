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




class Person:
    def __init__(self, name, age, address):
        self.name, self.age, self.address = name, age, address

    def greeting(self):
        return f"Hello, my name is {self.name}."

    def __str__(self):
        return f"{self.name}, {self.age} years old, Address: {self.address}"

class Student(Person):
    def __init__(self, name, age, address, grade, major):
        super().__init__(name, age, address)
        self.grade, self.major = grade, major

    def greeting(self):
        return f"Hello, I'm {self.name}, a {self.major} student."

    def is_passed(self):
        return self.grade >= 60

    def __str__(self):
        return f"{super().__str__()}, Major: {self.major}, Grade: {self.grade}, Passed: {'Yes' if self.is_passed() else 'No'}"

# Example usage:
student = Student("Manha Binta Bellah", 11, "Mohammadpur,Dhaka", 100, "Game developer and Software Ingeneer")
print(student.greeting())  # Output: Hello, I'm Manha Binta Bellah, a Game developer and Software Ingenee




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, my name is {self.name} . I'm {self.age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return f"{super().introduce()} I am a student. My ID is{self.student_id}."

person = Person("Raisa", 13)
print(person.introduce())

print(person.introduce())  

student = Student("Emma", 20, "S92945")
print(student.introduce())





class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name}, and I am {self.age} years old."

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    def display_info(self):
        print(f'''
Name: {self.name}
age: {self.age}
grade: {self.grade}
                ''')

    # def get_grade(self):
    #     return f"{self.name} is in grade {self.grade}."

student = Student("Ahan", 17, 10)
# print(student.introduce())  # Output: My name is Ahan, and I am 17 years old.
print(student.display_info())  # Output: Ahan is in grade 10.




class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"I am {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.hobby = hobby

    def display_info(self):
        print(f"I am {self.name} and I am {self.age} years old. My hobby is {self.hobby}")

    def get_grade(self):
        return f"{self.name}'s Hobby is {self.hobby}."

Per_1 = Person("Anik",23)
Per_1.display_info()
Stu_1 = Student("Erik",12,"playing")
Stu_1.display_info()
print(Stu_1.get_grade())