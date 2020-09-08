# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

degree_sign = u"\N{DEGREE SIGN}"
# Taking the lengths of AB and AC
p = int(input("Enter the length of AB"))
b = int(input("Enter the length of BC"))
# Calculating the hypotenuse of the right angled triangle ABC
h = math.sqrt((p ** 2) + (b ** 2))
print(h)

# Getting the perpendicular value of MBC
h_small = h / 2
print(h_small)
# Getting the angle of B from triangle MBC
angle = math.asin((h_small / b))
angle = int(math.degrees(angle))
string = str(angle)
print(string + u"\N{DEGREE SIGN}")

