                                                              Sort 0s and 1s
 You are given an array of 0's and 1's. Sort the array in ascending order and print it.
Note: Solve using two-pointer technique.

Input Format

First line of input contains T - the number of test cases. Its followed by 2T lines, the first line contains N - the size of the array.
The second line contains the elements of the array.

Constraints

1 <= T <= 1000
1 <= N <= 1000
0 <= A[i] <= 1

Output Format

For each test case, sort the array in ascending order and print it on a new line.

Sample Input 0

2
5
0 1 1 0 1
6
1 1 1 1 1 0
Sample Output 0

0 0 1 1 1
0 1 1 1 1 1
  
  <================================= C++ SOLUTION ===============================================>
  
  #include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
void sort(int arr[],int n){
    int i=0,j=n-1;
    while(i<j){
        if(arr[i]==0 && arr[j]==1){
            i++;
            j--;
        }
        else if(arr[i]==1 && arr[j]==0){
            int temp=arr[i];
            arr[i]=arr[j];
            arr[j]=temp;
            i++;
            j--;
        }
        else if(arr[i]==0 && arr[j]==0){
            i++;
        }
        else{
            j--;
        }
    }
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
        sort(arr,n);
        for(int i=0;i<n;i++){
            printf("%d ",arr[i]);
        }
        printf("\n");
    }
    return 0;
}
