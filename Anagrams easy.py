t=int(input())
for i in range(t):
    a,b=map(str,input().strip().split())
    a1=list(a)
    b1=list(b)
    c=sorted(a1)
    d=sorted(b1)
    if(c==d):
        print("True")
    else:
        print("False")
