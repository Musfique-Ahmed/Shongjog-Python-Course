# Define a function
def myFunc(name = "unknown"): # parameter(variable): name = "Musfique" # default parameter: "unknown"
    # code block
    print("Hello World!")
    print(f"My name is {name}!")

# call the function
myFunc("Musfique") # Aegument: "Musfique"

myFunc()


# Default parameter
def area(height, width=3):
    print(f"The area of the rectangle is {height * width} meter.")

area(10, 5)
area(8)