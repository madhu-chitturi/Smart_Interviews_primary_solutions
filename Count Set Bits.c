                                                                                Count Set Bits
  /* Given a number N, find the number of bits that are set to 1 in its binary representation.

Input Format

First line of input contains T - the number of test cases. It is followed by T lines, each line contains a single integer N.

Constraints

1 <= T <= 104
0 <= N <= 1018

Output Format

For each test case, print the number of bits set to 1 in the binary representation of N, separated by a new line.

Sample Input 0

3
4
15
10
Sample Output 0

1
4
2
Explanation 0

Test-Case 1:
The binary representation of 4 is 100. The number of 1's in the binary representation of 4 is 1.

Test-Case 2:
The binary representation of 15 is 1111. The number of 1's in the binary representation of 15 is 4.*/

<============================== C SOLUTION =====================================>

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
long long checkbit(long long n){
    long long count=0;
    while(n!=0){
        if((n&1)==1){
            count++;
        }
        n=n>>1;
    }
    return count;
}
int main() {    
    long long t;
    scanf("%lld",&t);
    while(t--){
        long long n;
        scanf("%lld",&n);
        printf("%lld\n",checkbit(n));
    }
    return 0;
}


<===============================PYTHON SOLUTION ================================>

t=int(input())
for i in range(t):
    n=int(input())
    b=bin(n)
    c=(b[2:])
    arr=list(c)
    count=0
    for j in range(len(arr)):
        if(arr[j]=='1'):
            count+=1
    print(count)
