 /*                                                           Print Right Angled Triangle Pattern
 Print mirror image of right-angled triangle using '*'. See examples for more details.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each line contains a single integer N - the size of the pattern.

Constraints

1 <= T <= 100
1 <= N <= 100

Output Format

For each test case, print the test case number as shown, followed by the pattern, separated by newline.

Sample Input 0

4
2
1
5
10
Sample Output 0

Case #1:
 *
**
Case #2:
*
Case #3:
    *
   **
  ***
 ****
*****
Case #4:
         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********
**********                              */

SOLUTION<======================= C =====================>

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        int n;
        scanf("%d",&n);
        printf("Case #%d:\n",i+1);
        for(int i=0;i<n;i++){
                for(int j=0;j<n-i-1;j++){
                    printf(" ");
                }
            for(int k=0;k<i+1;k++){
                printf("*");
            }
            printf("\n");
        }
        
    }
    return 0;
}


<============================PYTHON SOLUTION==============================>

t = int(input())
for i in range(t):
    y = int(input())
    print("Case #" + str(i+1) + ":", end="")
    for i in range(y + 1):
        for j in range(y-i, 0, -1):
            print(" ", end="")
        for k in range(1, i+1):
            print("*", end="")
        print()
