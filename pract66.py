n=int(input("Enter any number"))

def fibbonacci(n):
    t=0
    a=0
    b=1
    for i in range(1,n+1):
        print(a)
        t=a+b
        a=b
        b=t
    return a
    
    

fibbonacci(n)