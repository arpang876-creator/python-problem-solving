#sum of first n natural numbers

def sum_recurs(n):
    if(n==0):
        return 0
    else:
        return sum_recurs (n-1)+n
    

print(sum_recurs(2))


print(sum_recurs(5))