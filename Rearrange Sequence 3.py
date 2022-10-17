                                                  Rearrange Sequence 3
  You are given an array of size N containing integers. Find the size of the largest subarray that can be rearranged to form a continguous sequence.
A continguous sequence means that the difference of adjacent elements should be 0 or 1.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N - the size of the array.
The second line contains the elements of the array.

Constraints

1 <= T <= 100
1 <= N <= 1000
0 <= A[i] <= 105

Output Format

For each test case, print the size of the largest subarray that can be rearranged to form a continguous sequence, on a new line.

Sample Input 0

2
10
15 13 14 8 5 2 3 3 1 1
9
8 8 6 7 3 5 7 4 1
Sample Output 0

5
8
Explanation 0

Test-Case 1
The largest subarray which can be rearranged to form a continguous sequence is [2, 3, 3, 1, 1] which can be rearranged to form [1, 1, 2, 3, 3].

Test-Case 2
The largest subarray which can be rearranged to form a continguous sequence is [8, 8, 6, 7, 3, 5, 7, 4] which can be rearranged to form [3, 4, 5, 6, 7, 7, 8, 8].
  
  <==================================== PYTHON SOLUTION ======================================>
  
  t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().strip().split()))
    ans=0
    for j in range(n):
        hs={}
        max1=-2147483648
        min1=2147483647
        for k in range(j,n):
            hs[l[k]]=1
            max1=max(l[k],max1)
            min1=min(l[k],min1)
            if(max1-min1+1==len(hs)):
              ans=max(ans,k-j+1)
    print(ans)
