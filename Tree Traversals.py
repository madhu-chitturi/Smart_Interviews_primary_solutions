                                                              Tree Traversals
  
  class Node:
    def __init__(this,val): 
        this.val = val 
        this.left = None  
        this.right = None 
def preorder(root):
    if(root==None):
        return
    print(root.val,end=" ")
    preorder(root.left)
    preorder(root.right)
def postorder(root):
    if(root==None):
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val,end=" ")
def inorder(root):
    if(root==None):
        return
    
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)
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
    preorder(root)
    print()
    inorder(root)
    print()
    postorder(root)
    print()
    print()
