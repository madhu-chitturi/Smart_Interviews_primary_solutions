t=int(input())
top=-1
arr=[]
for i in range(t):
    x=list(input())
    n=len(x)
    if(x[1]=='u'):
        top+=1
        index=x.index(' ')
        m=x[index+1:]
        o=m[0]
        for y in range(1,len(m)):
            o+=m[y]
        arr.insert(top,int(o))
    else:
        if(top==-1):
            print("Empty")
        else:
            print(arr[top])   
            top-=1          
            

        
