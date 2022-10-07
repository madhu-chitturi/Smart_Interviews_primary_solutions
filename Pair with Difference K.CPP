                                                                    Pair with Difference K

You are given an integer array and a positive integer K. You have to tell if there exists a pair of integers in the given array such that ar[i]-ar[j]=K and i≠j.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N and K - the size of the array and the number K. The second line contains the elements of the array.

Constraints

40 points
2 <= N <= 1000

60 points
2 <= N <= 100000

General Constraints
1 <= T <= 100
-105 <= ar[i], K <= 105

Output Format

For each test case, print "true" if the arrays contains such elements, false otherwise, separated by new line.

Sample Input 0

2
5 60
1 20 40 100 80 
10 11
12 45 52 65 21 645 234 14 575 112 
Sample Output 0

true
false
  
  
  <================================= C++ SOLUTION =================================>
  
  #include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int pairdiff(int arr[],int n,int k){
    int i=0,j=0;
    while(i<n && j<n){
        if(arr[i]-arr[j]==k){
            return 1;
            break;
        }
        else if(arr[i]-arr[j]<k){
            i++;
        }
        else{
            j++;
        }
    }
    return 2;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int t;
    scanf("%d",&t);
    while(t--){
        int n,k;
        scanf("%d%d",&n,&k);
        int arr[n];
        for(int i=0;i<n;i++){
            scanf("%d",&arr[i]);
        }
        sort(arr,arr+n);
        if(pairdiff(arr,n,k)==1){
            printf("true\n");
        }
        else{
            printf("false\n");
        }
    }
    return 0;
}
