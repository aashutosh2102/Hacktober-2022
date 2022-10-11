def fact(n):
    if n==1:
        return 1
    else: 
        for i in range (n):
            a=n*fact(n-1)
            return a

       
n=int(input("enter a number: "))
print(fact(n))