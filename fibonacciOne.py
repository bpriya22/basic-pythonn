a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))
n=int(input("enter the number of elements:"))
print(a,b,end=" ")
while n-2:
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-1