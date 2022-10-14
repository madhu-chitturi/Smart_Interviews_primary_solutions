                                                                  Repeated Numbers
        
You are given an array of N elements. All elements of the array are in range 1 to N-2. All elements occur once except two numbers, which occur twice. Your task is to find the two repeating numbers.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N - the size of the array and second line contains the elements of the array.

Constraints

30 points
1 <= T <= 100
4 <= N <= 103

70 points
1 <= T <= 100
4 <= N <= 106

Output Format

Print the 2 repeated numbers in sorted manner, for each test case, separated by new line.

Sample Input 0

2
8
1 3 2 3 4 6 5 5 
10
1 5 2 8 1 4 7 4 3 6 
Sample Output 0

3 5
1 4
  
 <============================= C SOLUTION =============================>
 
  #include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
void countsort(int arr[],int n){
    int cnt[n];
    for(int i=0;i<n;i++){
        cnt[i]=0;
    }
    for(int i=0;i<n;i++){
        cnt[arr[i]]++;
    }
    for(int i=0;i<n;i++){
        arr[i]=cnt[i];
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
        countsort(arr,n);
        for(int i=0;i<n;i++){
            if(arr[i]==2){
                printf("%d ",i);
            }
        }
        printf("\n");     
    }
    return 0;
}
