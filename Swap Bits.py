                                                                  Swap Bits
Given a number, swap the adjacent bits in the binary representation of the number, and print the new number formed after swapping.

Input Format

First line of input contains T - number of test cases. Each of the next T lines contains a number N.

Constraints

1 <= T <= 100000
0 <= N <= 109

Output Format

For each test case, print the new integer formed after swapping adjacent bits, separated by new line.

Sample Input

4
10
7
43
100

Sample Output

5
11
23
152

Explanation

Test Case 1

Binary Representation of 10: 000...1010
After swapping adjacent bits: 000...0101 (5)

Test Case 2

Binary Representation of 7: 000...0111
After swapping adjacent bits: 000...1011 (11)
  
 <==================PYTHON SOLUTION================>

t=int(input())
for i in range(t):
    n=int(input())
    a=bin(n)
    b=list(a)
    b.remove(b[0])
    b.remove(b[0])
    if(len(b)%2!=0):
        b.insert(0,'0')
    i=0
    while(i<len(b)):
        temp=b[i]
        b[i]=b[i+1]
        b[i+1]=temp 
        i+=2
    s='0'
    for k in range(len(b)):
        s+=b[k]
    m=int(s,2)
    print(m)
    
    
