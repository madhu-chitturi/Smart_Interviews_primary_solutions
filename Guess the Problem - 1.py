

t=int(input())
for _ in range(t):
    a,b=list(map(str,input().strip().split()))
    dict1={}
    for i in range(len(a)):
        if a[i] in dict1:
             dict1[a[i]]+=1
        else:
             dict1[a[i]]=1
    for j in range(len(b)):
        if b[j] not in dict1:
             print(b[j],end="")
    print()
    
