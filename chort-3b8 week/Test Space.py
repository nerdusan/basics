import keyword

print ("These are the requested keywords sir. \n")
print (keyword.kwlist)


#None

None == 0
print(None)


#True and False
def improper(a):
    if (a%3)==0:
     return True
    elif (a%3)!=0:
         return False
x = improper(2)
print (x)

y = (True or False)
print (y)



#import, as

import math as mayorkun
mayorkun.cos(mayorkun.pi)
print(mayorkun.pi)
w = (mayorkun.pi)
print(mayorkun.cos(w))


