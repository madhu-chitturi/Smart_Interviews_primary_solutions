                                                                    Trailing Zeros Easy

Count the number of trailing 0s in factorial of a given number.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each containing an integer N.

Constraints

1 <= T <= 10000
1 <= N <= 1015

Output Format

For each test case, print the number of trailing 0s in N!, separated by new line.

Sample Input 0

3
2
5
20
Sample Output 0

0
1
4
Explanation 0

2! = 2 [No trailing zeros]
5! = 120 [Trailing zeros=1]
20! = 2432902008176640000 [Trailing zeros=4]

<============================== PYTHON SOLUTION ==============================>

t=int(input())
for i in range(t):
    n=int(input())
    if(n < 0):
        print("0")
    count = 0
    while(n >= 5):
        n //= 5
        count += n
    print(count)
 
