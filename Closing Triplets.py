import math
t=int(input())
for _ in range(t):
    n1=int(input())
    a=list(map(int,input().strip().split()))
    n2=int(input())
    b=list(map(int,input().strip().split()))
    n3=int(input())
    c=list(map(int,input().strip().split()))
    p1=0
    p2=0
    p3=0
    A=sorted(a)
    B=sorted(b)
    C=sorted(c)
    ans=10000000007
    while(p1<n1 and p2<n2 and p3<n3):
        max1=max(A[p1],B[p2],C[p3])
        min1=min(A[p1],B[p2],C[p3])
        diff=max1-min1
        ans=min(ans,diff)
        if(min1==A[p1]):
            p1+=1
        elif(min1==B[p2]):
            p2+=1
        else:
            p3+=1
    print(ans)
    
    
    
