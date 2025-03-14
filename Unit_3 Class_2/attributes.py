class Car:
    wheels = 4 # Class variable

    def __init__(self, brand, model, color): # Constructor
        self.brand = brand # Instance Variable
        self.model = model
        self.color = color

    def display(self): # Instance Methods
        print(f"Now you own a {self.brand} {self.model} {self.color} which has {self.wheels} wheels!")

    def define_data_items(self, year_made, no_of_doors, size_of_engine):
        self.year_made = year_made

    def change_a_data(self, color=None, size_of_engine = None):
        if color: self.color = color
        if size_of_engine: self.size_of_engine = size_of_engine

    def can_go_fast(self, speed):
        if speed >= 150:
            print(f"The {self.brand} {self.model} can go really fast!")
        else:
            print(f"The {self.brand} {self.model} can't go fast!")

    def is_electric(self):
        if self.brand == "Tesla":
            print(f"This is an electric car!")
        else:
            print(f"This is not an electric Car!")

lambargini = Car("Lambargini", "Urus", "Yellow")
lambargini.can_go_fast(300)
# lambargini.is_electric()
lambargini.display()


farari = Car("farari", "458 Pista", "Red")
# farari.can_go_fast(250)
farari.display()




    # def define_data_items(self, year_made, no_of_doors, size_of_engine):
    #     self.year_made = year_made

    # def change_a_data(self, color=None, size_of_engine = None):
    #     if color: self.color = color
    #     if size_of_engine: self.size_of_engine = size_of_engine

    # def can_go_fast(self, speed):
    #     if speed >= 150:
    #         print(f"The {self.brand} {self.model} can go really fast!")
    #     else:
    #         print(f"The {self.brand} {self.model} can't go fast!")

    # def is_electric(self):
    #     if self.brand == "Tesla":
    #         print(f"This is an electric car!")
    #     else:
    #         print(f"This is not an electric Car!")