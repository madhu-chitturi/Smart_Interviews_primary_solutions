

t=int(input())
for i in range(t):
    a,b=list(map(str,input().strip().split()))
    k=int(b)
    for j in range(len(a)):
        z=ord(a[j])
        y=z-97
        x=y+k
        w=x%26
        print(chr(w+97),end="")
    print()
