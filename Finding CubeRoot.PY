                                                                        FINDING CUBEROOT
 Find the cube root of the given number. Assume that all the input test cases will be a perfect cube.
Note: Do not use any inbuilt functions/libraries for your main logic.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each containing a single integer.

Constraints

30 points
1 <= T <= 103
-109 <= N <= 109

70 points
1 <= T <= 106
-1018 <= N <= 1018

Output Format

For each test case, print the cube root of the number, separated by newline.

Sample Input 0

5
-27
-125
1000
6859
-19683
Sample Output 0

-3
-5
10
19
-27

<============================================= PYTHON SOLUTION ======================================>

def cuberoot(x):
    if x < 0:
        x = abs(x)
        cube_root = x**(1/3)*(-1)
    else:
        cube_root = x**(1/3)
    return cube_root
t=int(input())
for i in range(t):
    n=int(input())
    print(round(cuberoot(n)))
