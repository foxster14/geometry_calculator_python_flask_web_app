import math

def slant(radius, height):
    slant = round(math.sqrt(radius**2 + height**2),2)
    return slant

def surface(radius, height):
    surfaceArea = round(math.pi * radius * (radius + math.sqrt(height**2 + radius**2)),2)
    return surfaceArea

def volume(radius, height):
    volume = round(math.pi * radius**2 * (height/3),2)
    return volume

def lateral(radius, height):
    lateral = round(math.pi * radius * math.sqrt(height**2 + radius**2),2)
    return lateral

