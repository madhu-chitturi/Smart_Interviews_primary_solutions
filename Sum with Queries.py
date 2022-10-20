t=int(input())
for d in range(t):
    n=int(input())
    arr=list(map(int,input().strip().split()))
    temp=[0 for f in range(n)]
    q=int(input())
    for e in range(q):
        i,j,x=map(int,input().strip().split())
        if j<n-1:
            temp[i]+=x
            temp[j+1]-=x
        else:
            temp[i]+=x
    for i in range(1,n):
        temp[i]+=temp[i-1]
    for i in range(n):
        arr[i]=arr[i]+temp[i]
    print(sum(arr))
