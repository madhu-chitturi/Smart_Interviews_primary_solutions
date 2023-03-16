class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def insert(root,x):
    if(root==None):
        n=Node(x)
        return n
    else:
        if(x<=root.val):
            a=insert(root.left,x)
            root.left=a
        else:
            a=insert(root.right,x)
            root.right=a
        return root
def Level(root,d):
    idx=0
    q=[]
    q.append(root)
    d[idx]=[root.val]
    q.append('!')
    while(len(q)>0):
        n=q[0]
        q.pop(0)
        if(n=='!'):
            if(len(q)!=0):
                idx+=1
                q.append('!')
        else:
            if idx in d:
                d[idx].append(n.val)
            else:
                d[idx]=[n.val]
            if(n.left):
                q.append(n.left)
            if(n.right):
                q.append(n.right)
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().strip().split()))
    root=None
    for j in range(n):
        x=arr[j]
        root=insert(root,x)
    d={}
    Level(root,d)
    for i in range(len(d)):
        a=d[i]
        print(a[0],end=" ")
    print()
