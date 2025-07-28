def fibon(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibon(n-1)+fibon(n-2)
    
n=4
for i in range(1,n+1):
    print(fibon(i))