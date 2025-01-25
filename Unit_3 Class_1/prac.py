#AHAN
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def output(self):
        print(f"Car Details:\nBrand: {self.brand}\nModel: {self.model}\nColor: {self.color}")


my_car = Car("Toyota", "Harrier", "Wine Red")
my_car_1 = Car("Honda", "CHR", "Pearl")
my_car_3 = Car("Honda", "CRV", "Black")
my_car.output()
my_car_1.output()
my_car_3.output()

# Farzia Lopa
# 7:58 PM
class Car:
    def __init__(self, brand, model, colour):
        self.brand = brand
        self.model = model
        self.colour = colour

    def display_info(self):
        print(f" Insha Allah my future car is a {self.colour.lower()} {self.brand} {self.model.title()}")

# Example usage:
my_car = Car("Tesla", "Model S", "red")
my_car.display_info()

# cade (Shakib)
# 8:00 PM
class Car:
    def __init__(self, brand, model, colour):
        self.brand = brand
        self.model = model
        self.colour = colour

    def display_info(self):
        print(f"  my future car is {self.colour.lower()} {self.brand} {self.model.title()}")

# Example usage:
my_car = Car("Ferrari", "f40", "red")
my_car.display_info()


# Musyab Iqbal
# 8:02 PM
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color


    def display_info(self):
        print(f"my car is {self.color.lower()} {self.brand} {self.model.title()}")

my_car = Car("Tesla","Model X","red")
my_car.display_info()

# Anjonavo Nilim
# 8:02 PM
class Car: #the first letter of a class will be capital
    def __init__(self,brand,model,color): #Follow dunder method(double underscore)
        self.brand = brand
        self.model = model
        self.color = color
    def display_info(self):
        print(f" My Car is {self.color.lower()} {self.brand} {self.model.title()}")

my_car = Car("Ferrari", "458 Pista", "Red")
my_car.display_info()

# Raisa
# 8:05 PM
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    
    def display_info(self):
        print(f" The {self.color} color {self.brand} is my dream")


my_car = Car("Tesla", "Model X", "red")
my_car.display_info()


# Bazlur Sohag
# 8:11 PM
class Car:
    def __init__(self, brand, model, color):
                self.brand = brand
                self.model = model
                self.color = color
    def display_info(self):
        print(f" My Car is {self.color.lower()} {self.brand} {self.model.title()}")

Ferrari = Car("Ferrari", "458 Pista", "red")
Ferrari.display_info()


# Jimisha
# 8:18 PM
class Car:
    def __init__(self, colour, model):
        self.color=colour 
        self.model=model
    def display_info(self):
      print(f"My Car is {self.color.lower()} {self.model.title()}")
 
# car=("8900fx","red")
my_car = Car("Red", "X Corolla")
# car.disply_info()
my_car.display_info()


# if change in ["Emotion", "Reflection", "Date_Time"]:
#     new_value = input(f"Enter the new value for {change}: ").strip()
#     # Updated_value = change.replace(change, new_value)


#     file = open("User_info.txt","r")
#     content = file.read()
#     file.close()
#     Updated_value = content.replace(change, new_value)
#     file = open("User_info.txt","w")
#     file.write(Updated_value)
#     file.close()

# used this for this(source-yt,geeks,)
# else:
#     print("Invalid key. Please choose 'Emotion', 'Reflection', or 'Date_Time'.")