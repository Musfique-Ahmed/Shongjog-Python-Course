class Shapes: #Parent Class
    def __init__(self):
        pass
    def calculate_area(self):
        print("Calculating Area!")

class Circle(Shapes): #Child Class-1
    def __init__(self, radious):
        self.radious = radious

    # 3.1416 * radious**2
    def calculate_area(self): #Method over riding
        return 3.1416 * self.radious**2

class Square(Shapes): #Child Class-2
    def __init__(self, lenght):
        self.lenght = lenght

    # lenght**2
    def calculate_area(self): #Method over riding
        return self.lenght**2
    

c_1 = Circle(5)
s_1 = Square(5)

print(c_1.calculate_area())
print(s_1.calculate_area())



# Musyab Iqbal
# 7:11 PM
class Bird:
    def fly():
        return "Some birds can fly"

class Eagle(Bird):
    def fly():
        return "Can fly"

class Penguin(Bird):
    def fly():
        return "Cannot fly"

print("Eagle:", Eagle.fly())    # Output: Can fly
print("Penguin:", Penguin.fly()) # Output: Cannot fly



# Farzia Lopa
# 7:12 PM
class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        # Default behavior for Bird class
        print(f"{self.name} can fly in general.")

# Eagle class that overrides the fly() method
class Eagle(Bird):
    def fly(self):
        print("Can fly")

# Penguin class that overrides the fly() method
class Penguin(Bird):
    def fly(self):
        print("Cannot fly")

# Example usage:
eagle = Eagle("Eagle")
eagle.fly()  # Output: Can fly

penguin = Penguin("Penguin")
penguin.fly()

# Musyab Iqbal
# 7:11 PM
# Loafz
# 7:13 PM
class Bird:
    def fly():
        return "A bird can fly."

class Eagle(Bird):
    def fly():
        return "A eagle can fly."

class Penguin(Bird):
    def fly():
        return "A penguin can not fly."

print("Eagle:", Eagle.fly()) 
print("Penguin:", Penguin.fly())




# AHAN
class Bird: #parent class
    def __init__(self, name):
        self.name = name

    def fly(self):
        return "Some birds can fly"

class Eagle(Bird):
    def __init__(self, name):
        super().__init__(name)

    def fly(self): #method over riding
        return "Can fly"

class Penguin(Bird):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        return "Cannot fly"
    

eagle = Eagle("Eagle")
penguin = Penguin("Penguin")

print(f"{eagle.name}: {eagle.fly()}")   # Output: Eagle: Can fly
print(f"{penguin.name}: {penguin.fly()}") # Output: Penguin: Cannot fly
