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
def Level(root):
    q=[]
    q.append(root)
    q.append('!')
    while(len(q)>0):
        n=q[0]
        q.pop(0)
        if(n=='!'):
            print()
            if(len(q)!=0):
                q.append('!')
        else:
            print(n.val,end=" ")
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
    Level(root)
    print()
