ans=0
def partion(a,n,k):
    global ans
    l=min(a)
    h=sum(a)
    while(l<=h):
        m=(l+h)//2
        if(isvalid(a,n,k,m)==1):
            ans=m
            h=m-1
        else:
            l=m+1
def isvalid(arr,n,k,mid):
    s=0
    p=1
    for i in arr:
        if i>mid:
            return 0
        elif(s+i>mid):
            s=i
            p+=1
        else:
            s+=i
    if p<=k:
        return 1
    return 0
for _ in range(int(input())):
    n,k=map(int,input().strip().split())
    l=list(map(int,input().strip().split()))
    partion(l,n,k)
    print(ans)
