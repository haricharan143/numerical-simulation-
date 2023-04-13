##funtion basics
def add(a,b,c):
    sum=a+b+c
    return sum
print(add(3,3,3))
n = 42
def func():
    global n
    print(f'Within function: n is {n}')
    n = 3
    print(f'Within function: change n to {n}')
func()
print(f'Outside function: Value of n is {n}')
##lambda funtions
s=lambda x:x**2
print(s(3))
adder=lambda x,y: x+y
print(adder(1,2))
##problems
#1
import numpy as np
def my_sinh(x):
    y=(np.exp(x)-np.exp(-x))/2
    return y
print(my_sinh(0))
print(my_sinh(1))
#2
def my_checker_board(n):
    pattern = [1, 0] * ((n + 1) // 2)
    rows = [pattern[i % len(pattern):] + pattern[:i % len(pattern)] for i in range(n)]     
    checkerboard = np.array(rows)
    return checkerboard
print(my_checker_board(1))
#3
def my_triangle(b, h):
    area = 0.5 * b * h
    return area
print(my_triangle(1,1))
print(my_triangle(2,1))
#4
import math
def my_cylinder(r,h):
    s=(2*math.pi*r*r)+(2*math.pi*r*h)
    v=math.pi*r*r*h
    return [s,v]
print(my_cylinder(1,5))

    