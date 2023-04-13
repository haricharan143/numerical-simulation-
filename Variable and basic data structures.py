##string
s="i love python"
print(type(s))
print(len(s))
print(s[6:11])
print(s.upper())
##list
l1=[1,2,3,4,5]
l1.append(11)
l2=["fruits","veggies"]
print(l1+l2)
print(l1)
##tuples
t1=(1,2,3,4,5)
print(len(t1))
print(t1)
##sets
s1=set([1,3,4,5,6])
print(set("banana"))
print(s1)
##dictionries
d1={"fruits":130,"school":121,"friends":0}
print(d1)
print(d1.keys())
print(d1.values())
##intoduction to numpy
import numpy as np
a=np.array([1,2])
print(a)
b=np.array([[1,2,3],[3,4,5],[1,6,5]])
print(b)
print(b.shape)
print(b.size)
c=np.arange(1,2000,1)
print(c)
print(b[1])
d=np.array([[1, 2],[3, 4]])
e=np.array([[3, 4],[5, 6]])
print(d*e)
print(d+e)
##problems
#1
S = '123'
N = float(S)
print(type(S))  
print(type(N))
#2
s1='HELLO'
s2='hello'
print(s1==s2)  
print(s1.lower()==s2)  
print(s1==s2.upper()) 
#3
l1=[1,8,9,15]
l1.insert(1,2)
l1.append(4)
print(l1)
#4
s1="python is great"
print(list(s1))
#5
set_a=set([2,3,2])
set_b=set([1,2,3])
union=set_a.union(set_b)
intersection=set_a.intersection(set_b)
difference=set_a.difference(set_b)
print(union)
print(intersection)
print(difference)
#6
import numpy as np
x=np.array([1,4,3,2,9,4])
y=np.array([2,3,4,1,2,3])
if x==y:
    print("both are same")
else:
    print("both are not same")

