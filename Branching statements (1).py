##Branching statements
## if-else statements
def my_thermo(temp,desire_temp):
    if temp<desire_temp-5:
        print("heat")
    elif temp>desire_temp+5:
        print("AC")
    else:
        print("off")
print(my_thermo(76, 88))
#1
def adder(a,b,c):
    if not isinstance(a,(int, float) or isinstance(b(int,float) or isinstance(c,(int,float)))):
        raise TypeError("input numbers only")
    return a+b+c
print(adder(1,5,3))
#2
def define_number(a):
    if a%2==0:
        status="its even"
    else:
        status="its odd"
    return status
print(define_number(12))
#3
import numpy as np
def my_circ_calc(r, calc):
    if calc=='area':
        return np.pi*r**2
    elif calc=='circumference':
        return 2*np.pi*r
print(my_circ_calc(2.5, 'area'))
print(my_circ_calc(3, 'circumference'))
##problems
#1
def my_tip_calculate(bill,party):
    if party<6:
        tip=bill*15/100
    elif party<8:
        tip=bill*18/100
    elif party<11:
        tip=bill*20/100
    elif party>11:
        tip=bill*25/100
    return tip
print(my_tip_calculate(109.29, 3))
#2
def my_mult_operation(a,b,operation):
    if operation=="minus":
        return a-b
    elif operation=="addition":
        return a+b
    elif operation=="multiplication":
        return a*b
    elif operation=="div":
        return a/b
    elif operation=="pow":
        return a**b
print(my_mult_operation(2, 5,"multiplication"))
#3
def my_letter_grader(percentage):
    if percentage>97:
        return "A+"
    elif 93<percentage<97:
        return "A"
    elif 90<percentage<93:
        return "A-"
    elif 87<percentage<90:
        return "B+"
    elif 83<percentage<87:
        return "B"
    elif 80<percentage<83:
        return "B-"
    elif 77<percentage<80:
        return "C+"
    elif 73<percentage<77:
        return "C"
    elif 70<percentage<73:
        return "C-"
    elif 67<percentage<70:
        return "D+"
    elif 63<percentage<67:
        return "D"
    elif 60<percentage<63:
        return "D-"
    else:
        return "F"
print(my_letter_grader(88))
#4
def my_nuke_alarm(s1, s2, s3):
    if abs(s1 - s2) > 10 and abs(s1 - s3) > 10:
        return 'alarm!'
    elif abs(s2 - s3) > 10:
        return 'alarm!'
    else:
        return 'normal'
print(my_nuke_alarm(94,96,90))

