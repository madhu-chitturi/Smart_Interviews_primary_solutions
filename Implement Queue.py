n=int(input())
rear=-1
front=-1
queue=[]
for i in range(n):
    x=list(input())
    if(x[0]=='E'):
        i=x.index(' ')
        m=x[i+1:]
        s=m[0]
        for j in range(1,len(m)):
            s+=m[j]
        rear=(rear+1)
        if(front==-1):
            front=0
        queue.insert(rear,int(s))
    else:
        if(front==-1):
            print("Empty")
        else:  
            print(queue[front])
            front=(front+1)
            if(front>rear):
                front=-1
                rear=-1
       
