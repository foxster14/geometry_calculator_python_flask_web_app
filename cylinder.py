# inspiration code for Python Unit Testing Project
# this code is the same exact file as used by the command line project
# it can just be imported as it by the web app
# and also still be used by itself

import math

def surfaceArea(radius, height):
    surfaceArea = (2 * math.pi * radius * height) + (2 * math.pi * radius**2)
    return surfaceArea

def volume(rad, hi):
    volume = math.pi * rad * rad * hi
    return volume

def lateral(radius, height):
    lateral = 2 * math.pi * radius * height
    return lateral

def base(radius):
    base = math.pi * radius**2
    return base

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
## This makes it so we can import the data from this file into our mainProgram.py
if __name__ == '__main__':
    prompt()