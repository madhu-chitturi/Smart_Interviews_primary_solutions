                                                          Rearrange Sequence 2
  You are given an array of size N containing integers which may not be unique. Find the size of the largest subarray that can be rearranged to form a strictly continguous sequence.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N - the size of the array. The second line contains the elements of the array.

Constraints

1 <= T <= 100
1 <= N <= 1000
0 <= A[i] <= 105

Output Format

For each test case, print the size of the largest subarray that can be rearranged to form a strictly continguous sequence, on a new line.

Sample Input 0

2
5
4 3 3 1 1
9
8 8 6 7 3 5 7 1 1
Sample Output 0

2
3
Explanation 0

Test-Case 1
The largest subarray which can be rearranged to form a strictly continguous sequence is {4, 3}, which can be rearranged to form {3, 4}.

Test-Case 2
The largest subarray which can be rearranged to form a strictly continguous sequence is {8, 6, 7}, which can be rearranged to form {6, 7, 8}.
  
  
  
  <============================== PYTHON SOLUTION ====================================>
  
  
  t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().strip().split()))
    ans=0
    for j in range(n):
        hm={}
        max1=-2147483648
        min1=2147483647
        for k in range(j,n):
            if arr[k] in hm:
                break
            hm[arr[k]]=1
            max1=max(max1,arr[k])
            min1=min(min1,arr[k])
            if(max1-min1==k-j):
                ans=max(ans,k-j+1)
    print(ans)
