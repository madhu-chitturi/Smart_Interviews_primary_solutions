                                                                 Find First Repeating Character - Variation
  Given a string of characters, find the first repeating character.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each line contains a single string of characters.

Constraints

1 <= T <= 1000
'a' <= str[i] <= 'z'
1 <= len(str) <= 104

Output Format

For each test case, print the first repeating character, separated by newline. If there are none, print '.'.

Sample Input 0

4
datastructures
algorithms
smartinterviews
hackerrank
Sample Output 0

a
.
t
r


<====================================== PYTHON SOLUTION ================================================>

t=int(input())
for i in range(t):
    s=list(input())
    l={}
    a="."
    for j in range(len(s)):
        if s[j] not in l:
            l[s[j]]=1
        else:
            a=s[j]
            break
    print(a)
