                                                                            Finding Frequency
Problem:
Given an array, you have to find the frequency of a number x.

Input Format

First line of input contains N - size of the array. The next line contains N integers, the elements of the array. The next line contains Q - number of queries. Each of the next Q lines contains a single integer X, for which you have to find the frequency of X in the given array.

Constraints

30 points
1 <= N <= 105
1 <= Q <= 102
-108 <= ar[i] <= 108

70 points
1 <= N <= 105
1 <= Q <= 105
-108 <= ar[i] <= 108

Output Format

For each query, print the frequency of X, separated by newline.

Sample Input 0

9
-6 10 -1 20 -1 15 5 -1 15 
5
-1
10
8
15
20
Sample Output 0

3
1
0
2
1

<==================================PYTHON SOLUTION {USING DICTIONARY}========================================>

''' USING HASH MAP(DICTIONARY)'''
n=int(input())
dict={}
arr1=list(map(int,input().strip().split()))
arr=sorted(arr1)
for i in range(n):
    if arr[i] in dict:
        dict[arr[i]]+=1
    else:
        dict[arr[i]]=1
q=int(input())
for j in range(q):
    x=int(input())
    if x in dict:
        print(dict[x])
    else:
        print("0")
