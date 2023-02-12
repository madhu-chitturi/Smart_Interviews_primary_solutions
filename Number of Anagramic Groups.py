<======= SOLUTION 1 =========>

t=int(input())
for _ in range(t):
    n,m=map(int,input().strip().split())
    dict1= {}
    strs=[]
    for i in range(n):
        strs.append(input())
    for i in strs:
        x = "".join(sorted(i))
        if x in dict1:
            dict1[x].append(i)
        else:
            dict1[x] = [i]
    k=list(dict1.values())
    print(len(k))
    
<=========  SOLUTION 2 ============>

t=int(input())
for _ in range(t):
    n,m=map(int,input().strip().split())
    l=[]
    for i in range(n):
        f=sorted(input())
        g="".join(f)
        l.append(g)
    h=set(l)
    print(len(h))
