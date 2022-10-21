
t=int(input())
for i in range(t):
    str1=input()
    li=str1.split()
    li1=list(reversed(li))
    for x in li1:
        print(x,end=" ")
    print()
