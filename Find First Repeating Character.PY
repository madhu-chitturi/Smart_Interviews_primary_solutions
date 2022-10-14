                                                               Find First Repeating Character 

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
s
a

<======================================= PYTHON SOLUTION ===============================================>

t=int(input())
for i in range(t):
    str1=list(input())
    cnt=[]
    a=0
    for j in range(26):
        cnt.append(0)
    for k in range(len(str1)):
        cnt[ord(str1[k])-97]+=1
    for z in range(len(str1)):
        if(cnt[ord(str1[z])-97]>1):
            a=1
            b=(ord(str1[z])-97)
            break
    if(a==0):
        print(".")
    else:
        x=b+97
        print(chr(x))
                                                              
