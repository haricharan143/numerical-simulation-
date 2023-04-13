##for loops
n = 0
for i in range(1, 4):
    n = n + i
print(n)
s = 0
a = [2, 3, 1, 3, 3]
for i in a:
    s=s+i
print(s)
##list comprehension
#1
x = range(5)
y = []
for i in x:
    y.append(i**2)
print(y)
#2
y = []
for i in range(5):
    for j in range(2):
        y.append(i + j)
print(y)

