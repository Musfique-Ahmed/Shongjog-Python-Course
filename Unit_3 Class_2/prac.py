# # Musyab
# class Student:
#     def __init__(self, name, grade, school):
#         self.name = name
#         self.grade = grade
#         self.school = school

#     def display(self):
#         print(f"Name: {self.name}, Grade: {self.grade}, School: {self.school}")


# student = Student("Musyab(without the y)", "A+","Noble School And College")
# student.display()

# # Nilim
# class Person:
#     school_name = "ABC High School"
#     def __init__(self,Name,Age):
#         self.Name = Name
#         self.Age = Age
#     def display_info(self):
#         print(f" I am {self.Name}, {self.Age} years old and my school anme is {self.school_name} .")

# my_info = Person("Nilim", 13 )
# my_info.display_info()

# # Ahan
# class Student:
#     school_name = "Willes Little Flower School and Collage"

#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     def display_info(self):
#         print(f"School Name: {Student.school_name}")
#         print(f"Student Name: {self.name}")
#         print(f"Grade: {self.grade}")

# student_1 = Student("Ahan", "10th Grade")
# student_1.display_info()
# student_2 = Student("Wachiu", "10th Grade")
# student_2.display_info()
# student_3 = Student("Saminur", "10")
# student_3.display_info()



# class Student:
#     school_name = "ABC High School"
#     def __init__(self, name, grade, school):
#         self.name = name
#         self.grade = grade
#         self.school = school
#     def display(self):
#         print(f"Name: {self.name}, Grade: {self.grade}, School: {self.school}")


# stu = Student("Raisa", "A+","ABC School")
# stu.display()


# class Student:
#     school_name = "Mohammadpur Preparatory School & College"

#     def __init__(self, name, grade):
#         self.name, self.grade = name, grade

#     def display_info(self):
#         print(f"{self.name} ({self.grade}) - {self.school_name}")

#     def update_grade(self, new_grade):
#         self.grade = new_grade

#     @classmethod
#     def change_school(cls, new_school):
#         cls.school_name = new_school

# # Example usage:
# student1 = Student("Manha Binta Bellah", "4th")
# student1.display_info()


# class Student:
#     school_name = "XYZ High School"
#     def __init__(self, name, grade, school):
#         self.name = name
#         self.grade = grade
#         self.school = school
#     def display(self):
#         print(f"Name: {self.name}, Grade: {self.grade}, School: {self.school}")
# stu = Student("Hamzaa Ibne Abdullah", "8","XYZ School")
# stu.display()


# class Student:
#     school_name = "narayanganj ideal school"
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#     def display_info(self):
#         print(f"School Name: {Student.school_name}")
#         print(f"Student Name: {self.name}")
#         print(f"Grade: {self.grade}")
# student_1 = Student("Daiyan", "7th Grade")
# student_1.display_info()
# student_2 = Student("mashur", "8th Grade")
# student_2.display_info()
# student_3 = Student("rafi", "10th Grade")


# # Ahan 
# class Rectangle:
#     school_name = "Area"
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     @property
#     def area(self):
#         return self.length * self.width

# rect = Rectangle(9, 8)
# print(rect.area)
# # Farzia Lopa
# # 7:41 PM
# class Rectangle:
#     def __init__(self, length, width):
#         self._length, self._width = length, width

#     @property
#     def area(self): return self._length * self._width

#     def __getattr__(self, attr): 
#         if attr == 'length': return self._length
#         if attr == 'width': return self._width
#         raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr}'")

# # Example usage:
# r = Rectangle(4, 6)
# print(r.area)  # Output: 24
# # AHAN Mahmud Towseem N
# # 7:42 PM
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     @property
#     def area(self):
#         return self.length * self.width

# rectangle = Rectangle(25, 8)
# print(f"Length: {rectangle.length}")    # Output: Length: 25
# print(f"Width: {rectangle.width}")      # Output: Width: 8
# print(f"Area: {rectangle.area}")        # Output: Area: 200



# # Md Ahnaf Rahman 21
# # 7:44 PM
# class rectangle:
#     def _init_(self , lenth , width):
#         self.lenth = lenth
#         self.width = width

#         @property
#         def area(self):
#             return self.lenth * self.width
        


# #EXAMPLE
# rectangle = Rectangle(25, 8)
# print(f"Length: {rectangle.length}")   
# print(f"Width: {rectangle.width}")      
# print(f"Area: {rectangle.area}")




class Circle:
    cirles = [] #Class variable [c1, c2]

    # Instance Method
    def __init__(self):
        Circle.cirles.append(self)
    
    # Static Method
    @staticmethod
    def calculate_area(radious):
        return 3.1416*radious**2

    # Class Method
    @classmethod
    def display(cls):
        print(f" In this class we have {len(cls.cirles)} circles")



c1 = Circle()
c2 = Circle()

print(c1.calculate_area(5))
print(c2.calculate_area(10))

Circle.display()

print(c1)