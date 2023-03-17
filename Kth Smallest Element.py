from heapq import heapify,heappop,heappush
t=int(input())
for i in range(t):
    n,k=map(int,input().strip().split())
    arr=list(map(int,input().strip().split()))
    hp=[]
    heapify(hp)
    for i in range(len(arr)):
        heappush(hp,arr[i])
    for j in range(k):
        x=heappop(hp)
    print(x)
