                                                                    Finding the Floor

Given an array, you have to find the floor of a number x. The floor of a number x is nothing but the largest number in the array less than or equal to x.

Input Format

First line of input contains N - size of the array. The next line contains N integers, the elements of the array. The next line contains Q - number of queries. Each of the next Q lines contains a single integer X, for which you have to find the floor of X in the given array.

Constraints

30 points
1 <= N <= 105
1 <= Q <= 102
-108 <= ar[i] <= 108

70 points
1 <= N <= 105
1 <= Q <= 105
-108 <= ar[i] <= 108

Output Format

For each query, print the floor of X, separated by newline. If floor not found, print the value of "INT_MIN"

Sample Input 0

6
-6 10 -1 20 15 5 
5
-1
10
8
-10
-4
Sample Output 0

-1
10
5
-2147483648
-6
  
  <============================= C++ SOLUTION =========================>
  
  #include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<limits.h>

using namespace std;
int floor(int arr[],int n,int x){
    int ans=INT_MIN;
    int low=0,high=n-1;
    while(low<=high){
        int mid=(low+high)/2;
        if(arr[mid]<=x){
            ans=arr[mid];
            low=mid+1;
        }
        else{
            high=mid-1;
        }    
    }
    return ans;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    sort(arr,arr+n);
    int q;
    scanf("%d",&q);
    for(int j=0;j<q;j++){
        int x;
        scanf("%d",&x);
        printf("%d\n",floor(arr,n,x));
    }
    return 0;
}
