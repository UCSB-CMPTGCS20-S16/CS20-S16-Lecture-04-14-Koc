def func(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i**2
    return(sum)

def func2(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + 1/i
    return(sum)

#-------------------------

def func3(n):
    prod = 1
    for i in range(2,n+1):
        prod = prod*i
    print(prod)

#-------------------------

def fun1(x,n):
    return(x**n)

def fun2(n,k):
    sum = 0
    for i in range(1,k+1):
        sum = sum + fun1(i,n)
    return(sum)

def fun3(m,n):
    prod = 1
    for j in range(1,m+1):
        prod = prod*fun2(n,j)
    return(prod)

#-------------------------

print(fun3(3,3))
