import turtle as t

def draw_square(distance):
    for i in range(4):
        t.forward(distance)
        t.left(90)
def draw_circle(radius):
    t.circle(radius)
def draw_triangle(distance):
    for i in range(3):
        t.forward(distance)
        t.left(120)
def draw_rectangle(distance):
    for i in range(2):
        t.forward(distance)
        t.right(90)
        t.forward(distance)
        t.right(90)
def main():
    t.speed(1)

    print("Choose a Shape To Draw")
    print("1.Square")
    print("2.Circle")
    print("3.Triangle")
    print("4.Rectangle")

    choice=input("Enter The Number Of The Shape: ")

    if choice in ["1","3","4"]:
        distance = int(input("Enter The Forward Distance:"))    
    elif choice in ["2"]:
        radius = int(input("Enter The Radius Of Your Circle:"))

    try:
        if choice == "1":
            draw_square(distance)
        elif choice == "2":
            draw_circle(radius)
        elif choice == "3":
            draw_triangle(distance)
        elif choice == "4":
            draw_rectangle(distance)
        else:
            print("Invalid choice! Please enter a number between 1 and 4!!!")
    except t.Terminator:
        print("The Turtle window was closed")


    t.done()
    
main()