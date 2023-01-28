t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().strip().split()))
    arr=sorted(arr)
    dict1={}
    for i in range(n):
        if arr[i] in dict1:
            dict1[arr[i]]+=1
        else:
            dict1[arr[i]]=1
    x=sorted(dict1.items(),key=lambda x:x[1])
    d=[]
    for a in range(len(x)):
        m=x[a]
        d.append(m[0])
    for i in range(len(d)):
        y=arr.count(d[i])
        for j in range(y):
            print(d[i],end=" ")
    print()
      
    
    
