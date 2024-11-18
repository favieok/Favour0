print("THIS IS A CODE TO PRINT PHYSICS AND MATHEMATICS OPERATIONS")

#VELOCITY
print("To solve for velocity, input your values in the following parameters")
def calculate_velocity():
    displacement = float(input("Input the value of displacement:"))
    time = float(input("Input the value of time:"))
    velocity = displacement / time
    print("Velocity is =" , velocity)
calculate_velocity()

#FORCE
print("To solve for force, input your values in the following parameters")
def calculate_force():
    mass = float(input("Input the value of mass:"))
    acceleration = float(input("Input the value of acceleration:"))
    force = mass * acceleration
    print("Force is =" , force)
calculate_force()

#SPEED
print("To solve for speed, input your values in the following parameters")
def calculate_speed():
        distance = float(input("Input the value of distance:"))
        time = int(input("Input the value of time:"))
        speed = distance / time
        print("Speed is =" , speed)
calculate_speed()

#AREA OF A RECTANGLE
print("To solve for area of a rectangle, input your values in the following parameters")
def calculate_area_of_a_rectangle():
    length = int(input("Input the value of length:"))
    width = int(input("Input the value of width:"))
    area_of_a_rectangle = length * width
    print("Area of a rectangle is =" , area_of_a_rectangle)
calculate_area_of_a_rectangle()

#PRESSURE
print("To solve for pressure, input your values in the following parameters")
def calculate_pressure():
    force = int(input("Input the value of base:"))
    area = int(input("Input the value of height:"))
    pressure = force / area
    print(pressure)
calculate_pressure()








