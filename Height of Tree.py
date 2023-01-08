                                                                      Height of Tree
  
 class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def height(root):
    if(root==None):
        return -1
    return max(height(root.left),height(root.right))+1
def insert(root,x):
    if(root==None):
        n=Node(x)
        return n
    if(x<root.val):
        root.left=insert(root.left,x)
    else:
        root.right=insert(root.right,x)
    return root
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().strip().split()))
    root=None
    for j in range(n):
        x=arr[j]
        root=insert(root,x)
    print(height(root))
    
    
