                                                                 Distinct elements in Window

Given an array of integers and a window size K, find the number of distinct elements in every window of size K of the given array.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - size of the array and K - size of the window. The second line contains N integers - elements of the array.

Constraints

1 <= T <= 1000
1 <= N <= 10000
1 <= K <= N
-100 <= ar[i] <= 100

Output Format

For each test case, print the number of distinct elements in every window of size K, separated by newline.

Sample Input 0

3
5 3
-2 -4 -2 4 -2 
10 7
3 -4 -3 -4 -2 0 2 -2 6 0 
17 13
-5 -1 4 8 -5 -3 -4 7 4 -4 0 8 0 -2 3 2 5 
Sample Output 0

2 3 2 
6 5 6 5 
8 9 9 10 11 


<==================================== PYTHON SOLUTION =======================================>

def window(arr,n,k):
    dict1={}
    c=[]
    for i in range(k):
        if arr[i] in dict1:
            dict1[arr[i]]+=1
        else:
            dict1[arr[i]]=1
    c.append(len(dict1))
    for j in range(k,n):
        dict1[arr[j-k]]-=1
        if(dict1[arr[j-k]]==0):
            del dict1[arr[j-k]]
        if arr[j] in dict1:
            dict1[arr[j]]+=1
        else:
            dict1[arr[j]]=1
        c.append(len(dict1))
    for z in c:
        print(z,end=" ")
    print()
        
t=int(input())
for i in range(t):
    n,k=map(int,input().strip().split())
    arr=list(map(int,input().strip().split()))
    window(arr,n,k)
