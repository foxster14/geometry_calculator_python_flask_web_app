import math # Makes the math library available

def surfaceArea(radius):
    surface=round((4 * math.pi * radius**2), 2)
    return surface

def volume(radius):
    volume=round(((4/3) * math.pi * radius**3), 2)
    return volume

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME AND SURFACE AREA OF SPHERE")
    print("------------------------------------------------------------")
    radius1 = int(input("Please Enter the radius :"))
    print("The Surface area of a Sphere = ", surfaceArea(radius1))
    print("The Volume of a Sphere = ", volume(radius1))

## Checks to see which program I am running and only invoke the prompt method if the name of this program is being run
## This makes it so we can import the data from this file into the main program
if __name__ == '__main__':
    prompt()
