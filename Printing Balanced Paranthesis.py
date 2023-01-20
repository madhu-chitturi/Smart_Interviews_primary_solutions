                                                                      Printing Balanced Paranthesis
  
  def printp(arr,n,oc,cc,idx):
    if(idx==n):
        for i in range(n):
            print(arr[i],end="")
        print()
        return
    if(oc<n/2):
        arr[idx]='{'
        printp(arr,n,oc+1,cc,idx+1)
    if(oc>cc):
        arr[idx]='}'
        printp(arr,n,oc,cc+1,idx+1)
t=int(input())
for i in range(t):
    print("Test Case #"+str(i+1)+":")
    n=int(input())
    n=n*2
    arr=[0 for x in range(n) ]
    printp(arr,n,0,0,0)
