/*                                            Sum of array elements
Problem
Submissions
Leaderboard
Given an array of integers, find the sum of the elements of the given array.
Note: Try to solve this without declaring/storing the array elements.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N - the size of the array and second line contains the elements of the array.

Constraints

1 <= T <= 100
1 <= N <= 1000
1 <= ar[i] <= 1015

Output Format

For each test case, print the sum of the elements of the array, separated by new line.

Sample Input 0

2
3
5 15 3 
2
70 100 
Sample Output 0

23
170  */


SOLUTION<========================  C ===================>

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    long long t;
    scanf("%lld",&t);
    while(t--){
        long long n;
        scanf("%lld",&n);
        long long arr[n],sum=0;
        for(long i=0;i<n;i++){
            scanf("%lld",&arr[i]);
            sum+=arr[i];
        }
        printf("%lld\n",sum);
        
    }
    return 0;
}


