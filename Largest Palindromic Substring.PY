                                                                  Largest Palindromic Substring 
  Given a string, find the length of the largest palindromic substring.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. The first line contains N - the size of the string and the second line contains a string of size N, containing only lowercase english alphabets.

Constraints

30 points
1 <= T <= 200
1 <= len(S) <= 102
'a' <= S[i] <= 'z'

70 points
1 <= T <= 200
1 <= len(S) <= 103
'a' <= S[i] <= 'z'

Output Format

For each test case, print the length of the largest palindromic substring, separated by newline.

Sample Input 0

5
8
pfyafafd
9
sllwffoqq
6
yoogvb
4
hcch
23
mzmqnnrkurfmmfrukrnnqsm
Sample Output 0

3
2
2
4
18
<================================ PYTHON SOLUTION ================================>

t=int(input())
for j in range(t):
    n=int(input())
    str1=input()
    ans=0
    for i in range(0,n):
        p1=i-1
        p2=i+1
        while(p1>=0 and p2<n and str1[p1]==str1[p2]):
            p1-=1
            p2+=1
        ans=max(ans,p2-p1-1)
        p1=i
        p2=i+1
        while(p1>=0 and p2<n and str1[p1]==str1[p2]):
            p1-=1
            p2+=1
        ans=max(ans,p2-p1-1)
    print(ans)
    
