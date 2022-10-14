                                                        Sum of Subarrays 
  Given an array of integers, answer queries of the form: [i, j] : Print the sum of array elements from A[i] to A[j], both inclusive.

Input Format

First line of input contains N - size of the array. The next line contains N integers - elements of the array. The next line contains Q - number of queries. Each of the next Q lines contains 2 space separated indexes: i and j.

Constraints

30 points
1 <= N,Q <= 10000

70 points
1 <= N,Q <= 500000

General Constraints
-109 <= A[i] <= 109
0 <= i <= j <= N-1

Output Format

For each query, print the sum of array elements from A[i] to A[j], both inclusive, separated by newline.

Sample Input 0

10
1 30 13 -4 -5 12 -53 -12 43 100 
4
0 5
1 7
2 3
7 9
Sample Output 0

47
-19
9
131

<========================================= PYTHON SOLUTION ==========================================>

n=int(input())
arr=list(map(int,input().strip().split()))
ps=[]
m=0
for i in range(n):
    m+=arr[i]
    ps.append(m)
q=int(input())
for j in range(q):
    i,j=map(int,input().strip().split())
    if(i>0):
        print(ps[j]-ps[i-1])
    else:
        print(ps[j])
