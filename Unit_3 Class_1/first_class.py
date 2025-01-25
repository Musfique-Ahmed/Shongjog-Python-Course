print("""
Task: Create a class named Car with the following:
    Attributes: brand, model, color.
Method: display_info() to print details of the car.

Example Output:
My car is a red Tesla Model S.
""")

class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

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
lambargini.is_electric()
