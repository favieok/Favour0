print("HELLO USER, THIS IS A CODE TO PERFORM PHYSICS AND MATHS OPERATIONS")
print("Choose options a, b, c, d or e to calculate velocity, force, pressure, speed and the area of a triangle respectively. ")
def a():
    #VELOCITY
    print("You have chosen to calculate velocity, input your values in the following parameters ")
    displacement = int(input("Input displacement:"))
    time = int(input("Input time:"))
    print("Velocity is =" , displacement / time)


def b():
    # FORCE
    print("You have chosen to calculate force, input your values in the following parameters ")
    mass = int(input("Input mass:"))
    acceleration = int(input("Input acceleration:"))
    print("Force is =", mass * acceleration)


def c():
    # PRESSURE
    print("You have chosen to calculate pressure, input your values in the following parameters ")
    force = int(input("Input force:"))
    area = int(input("Input area:"))
    print("Pressure is =", force / area)

def d():
    # SPEED
    print("You have chosen to calculate speed, input your values in the following parameters ")
    distance = int(input("Input distance:"))
    time = int(input("Input time:"))
    print("Speed is =", distance / time)

def e():
    # AREA OF A RECTANGLE
    print("You have chosen to calculate the area of a rectangle, input your values in the following parameters ")
    length = int(input("Input length:"))
    width = int(input("Input width:"))
    print("Area of the rectangle is =", length * width)

def main():
    answer = input("WHAT OPERATION WOULD YOU LIKE TO PERFORM?- ")

    if answer == "a":
        a()
    elif answer == "b":
        b()
    elif answer == "c":
        c()
    elif answer == "d":
        d()
    elif answer == "e":
        e()
    else:
        print("ERROR, TRY AGAIN...")
if __name__ == "__main__":
    main()