
def sum(n):
    if n==1:
        return 1
    else:
        for i in range(n):
            b=n+sum(n-1)
            return b
    

n=int(input("Enter a number: "))
a=sum(n)
print(a)