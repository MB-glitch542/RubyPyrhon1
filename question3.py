# Write a function fibonacci(n) that generates a list containing the first n numbers in the Fibonacci sequence.

def fibonacci(n):

    F=[]
    for i in range(n):
        if i==0:
            F.append(0)
        elif i==1:
            F.append(1)
        else:
            next_F=F[i-1]+F[i-2]
            F.append(next_F)
    return F
print(fibonacci(10))
