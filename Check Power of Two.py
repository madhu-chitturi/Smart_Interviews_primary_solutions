t=int(input())
for i in range(t):
    n=int(input())
    a=bin(n)
    b=list(a)
    if(b.count("1")==1):
        print("True")
    else:
        print("False")
