a = input ("Please enter term 'a' of equation: ")
b = input ("Please enter term 'b' of equation: ")
c = input ("Please enter term 'c' of equation: ")

a_int = int(a)
b_int = int(b)
c_int = int(c)

import math

discriminant = math.sqrt((b_int**2) - (4*a_int*c_int))
print (discriminant)

root1 = (0-b_int+discriminant)/(2*a_int)
root2 = (0-b_int-discriminant)/(2*a_int)

message = f"The roots of the equation are {root1} and {root2}"

print (message)