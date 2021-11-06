# inspiration code for Python Unit Testing Project
# this code is the same exact file as used by the command line project
# it can just be imported as it by the web app
# and also still be used by itself

import math

# calculate surface area using radius and height
def surfaceArea(radius, height):
    surfaceArea = round((2 * math.pi * radius * height) + (2 * math.pi * radius**2),2)
    # if type(radius) and type(height) != int:
    #     nullSurfaceArea = 0
    #     return nullSurfaceArea
    return surfaceArea

#calculate volume using radius and height
def volume(rad, hi):
    volume = round((math.pi * rad * rad * hi),2)
    # if type(rad) and type(hi) != int:
    #     nullVolume = 0
    #     return nullVolume
    return volume

# calculate lateral surface area using radius and height
def lateral(radius, height):
    lateral = round((2 * math.pi * radius * height),2)
    # if type(radius) and type(height) != int:
    #     nullLateral = 0
    #     return nullLateral
    return lateral

# calculate base (top or bottom of cylinder) surface area using radius
def base(radius):
    base = round((math.pi * radius**2),2)
    # if type(radius) != int:
    #     nullBase = 0
    #     return nullBase
    return base

# terminal output
def prompt():
    print()
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME & SURFACE AREA OF A CYLINDER")
    print("----------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))
    height = int(input("Please Enter the height :"))

    print("\nThe surface area of a cylinder =", round(surfaceArea(radius, height), 2))
    print("The volume of a cylinder =", round(volume(radius, height), 2))
    print("The lateral surface area of a cylinder =", round(lateral(radius, height), 2))
    print("The top OR bottom surface area of a cylinder =", round(base(radius), 2))

## Checks to see which program I am running and only invoke the prompt method if the name of this program is being run
## This makes it so we can import the data from this file into our GeometryCalcWeb.py
if __name__ == '__main__':
    prompt()