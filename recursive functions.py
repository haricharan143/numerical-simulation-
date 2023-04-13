##recursive functions
def fac(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fac(n-1)
print(fac(6))
#1
def fibonacci_display(n):
    if n == 1: 
        out = 1
        print(out)
        return out
    elif n == 2: 
        out = 1
        print(out)
        return out
    else: 
        out = fibonacci_display(n-1)+fibonacci_display(n-2)
        print(out)
        return out 
print(fibonacci_display(5))
##problems
#1
def my_ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return my_ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return my_ackermann(m - 1, my_ackermann(m, n - 1))
print(my_ackermann(1,1))
#2
def my_gcd(a, b):
    if b == 0:
        return a
    else:
        return my_gcd(b, a % b)
print(my_gcd(10, 4))
#3
def my_chebyshev_poly1(n, x):
    if n==0:
        return[1]*len(x)
    elif n==1:
        return x
    else:
        T0=[1]*len(x)
        T1=x
        for i in range(2, n+1):
            Tn=2*x* T1-T0
            T0,T1=T1,Tn
        return Tn
x = [1, 2, 3, 4, 5]
print(my_chebyshev_poly1(0,x))