                                                                                    Flip Bits
Problem:
You are given two numbers A and B. Write a program to count the number of bits to be flipped to change the number A to the number B. Flipping a bit of a number means changing a bit from 1 to 0 or vice versa.

Input Format

First line of input contains T - number of test cases. Each of the next T lines contains 2 integer A and B, separated by space.

Constraints

1 <= T <= 100000
0 <= N <= 109

Output Format

For each test case, print the number of bit flips required to convert A to B, separated by new line.

Sample Input 0

4
20 10
16 8
1 153
549 24
Sample Output 0

4
2
3
6
Explanation 0

Self Explanatory

Submissions: 11797
Max Score: 100
Difficulty: Easy
Rate This Challenge:

    
<========================= C SOLUTION =========================>

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int countset(int a,int b)
{
    int c=0;
    int r=a^b;
    while(r!=0){
        if((r&1)==1){
        c++;
        }
        r=r>>1;
    }
    return c;
}


int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int t;
    scanf("%d",&t);
    while(t--){
        int x,y;
        scanf("%d %d",&x,&y);
        printf("%d\n",countset(x,y));
    }
    return 0;
}

