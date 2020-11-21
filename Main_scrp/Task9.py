import cmath
from Res.task9_func import str_to_complex

a_raw = input("Please specify the \'a\' coefficient:\n")

if a_raw[-1].casefold() == ('i' or 'j'):
    a = str_to_complex(a_raw)
else:
    a = float(a_raw)

b_raw = input("Please specify the \'b\' coefficient:\n")

if b_raw[-1].casefold() == ('i' or 'j'):
    b = str_to_complex(b_raw)
else:
    b = float(b_raw)

c_raw = input("Please specify the \'c\' coefficient:\n")

if c_raw[-1].casefold() == ('i' or 'j'):
    c = str_to_complex(c_raw)
else:
    c = float(c_raw)

delta = b**2 - 4*a*c
x1 = (-b-1*cmath.sqrt(delta))/(2*a)
x2 = (-b+cmath.sqrt(delta))/(2*a)

print("First root of function is: " + str(x1))
print("Second root of function is: " + str(x2))
