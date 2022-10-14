                                                                  Rearrange Sequence 1
                                                                    
You are given an array of size N containing unique integers. Find the size of the largest subarray that can be rearranged to form a continguous sequence.
A continguous sequence means that the difference of adjacent elements should be 1.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N - the size of the array.
The second line contains the elements of the array.

Constraints

1 <= T <= 100
1 <= N <= 1000
0 <= A[i] <= 105

Output Format

For each test case, print the size of the largest subarray that can be rearranged to form a continguous sequence, on a new line.

Sample Input 0

2
5
1 3 2 6 5
9
0 8 6 5 7 10 3 2 1
Sample Output 0

3
4
Explanation 0

Test-Case 1
The largest subarray which can be rearranged to form a continguous sequence is [1, 3, 2], which can be rearranged to form [1, 2, 3].

Test-Case 2
The largest subarray which can be rearranged to form a continguous sequence is [8, 6, 5, 7], which can be rearranged to form [5, 6, 7, 8].
  
  
  <================================== C++ SOLUTION ==========================================>
  
  #include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<limits.h>
using namespace std;
int longest(int arr[],int n){
    int ans=0;
    for(int i=0;i<n;i++){
        int min1=INT_MAX;
        int max1=INT_MIN;
        for(int j=i;j<n;j++){
            min1=min(min1,arr[j]);
            max1=max(max1,arr[j]);
            if(max1-min1==j-i){
                ans=max(ans,j-i+1);
            }
        }
    }
    return ans;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int t;
    scanf("%d",&t);
    while(t--){
        int n;
        scanf("%d",&n);
        int arr[n];
        for(int i=0;i<n;i++){
            scanf("%d",&arr[i]);
        }
        printf("%d\n",longest(arr,n));
    }
    return 0;
}
