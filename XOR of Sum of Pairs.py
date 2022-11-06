                                                                            XOR of Sum of Pairs
                                                                            
                                                                            
def xor(arr, n) :
    ans = 0 
    for i in range(0, n) : 
            ans = ans ^(arr[i]) 
    return ans*2

t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().strip().split()))
    print(xor(arr,n))
