"""
Very simple program to test Python

Gilberto Echeverria
Python 3.4.2
"""


# Ask the user for his name
name = input("What is your name? ")

# Greet the user
print("Hello", name)

# Ask the user for some values to compute distance traveled
v = input("Speed: ")
# Convert the value entered from a string into a float (number with decimals)
v = float(v)
a = input("Acceleration: ")
a = float(a)
t = input("Time: ")
t = float(t)

# Calculate the distance
d = v * t + a * t**2 / 2

print("Distance traveled: ", d)
