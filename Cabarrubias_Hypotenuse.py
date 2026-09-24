import math as m # importing math as m makes the library be able to function as m.

# INPUT - The program asks for the length of side a and side b to find the hypotenuse of the triangle.
Side_A = float(input("What is the first side of the right triangle?: "))
Side_B = float(input("What is the second side of the right triangle?: "))

# PROCESS / CALCULATION
hypotenuse = m.sqrt(m.pow(Side_A, 2) + m.pow(Side_B, 2)) # Using m.sqrt (math.square root) and m.pow (math.power) to calculate the hypotenuse which would be the third side of the triangle.

# OUTPUT
print(f"The hypotenuse of your right triangle is: {hypotenuse:.2f}.") # This will display the answer it calculated in the processing stage. Using .2f, it will show the result up to 2 decimal places.
