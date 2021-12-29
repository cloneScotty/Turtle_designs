from turtle import *
from math import pi

def random_design(n, r, s):
    l = pi**2
    d = l*2
    a = d**pi
    speed(s)

    for i in range(int(a)):
        forward(l)
        right(d)
        forward(n)
        right(r)
        forward(i)
        right(r)
        forward(n-1)
        right(r+1)
        forward(n+1)
        right(r+2)
        n+=1

#SwagSurfin
random_design(150, 399, 10000)



