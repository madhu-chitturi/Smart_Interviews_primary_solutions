                                                                Is Full Binary Tree
  
  class Node:
    def __init__(this,val): 
        this.val = val 
        this.left = None  
        this.right = None 
def insert(root,x):
    if(root==None):
        n=Node(x)
        return n
    if(x<root.val):
        root.left=insert(root.left,x)
    else:
        root.right=insert(root.right,x)
    return root
def isFBT(root):
    if(root==None):
        return True
    if(root.left==None and root.right==None):
        return True
    if(root.left!=None and root.right!=None):
        return (isFBT(root.left) and isFBT(root.right))
    return False
    
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().strip().split()))
    root=None
    for j in range(n):
        x=arr[j]
        root=insert(root,x)
    print(isFBT(root))
        
