#求根公式
#! /usr/bin/env python3

import math
a = int(input('enter value of a:'))
b = int(input('enter value of b:'))
c = int(input('enter value of c:'))
d = b*b - 4*a*c
if d < 0:
    print('ROOTS are imaginary')
else:
    root1 = (-b + math.sqrt(d))/2*a
    root2 = (-b - math.sqt(d))/2*a
    print("Root 1 = ",root1)
    print("Root 2 = ",root2)
