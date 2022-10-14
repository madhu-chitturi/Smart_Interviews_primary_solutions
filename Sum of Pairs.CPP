                                                                        Sum of Pairs
                                                                        
                                                                        
Given an array of integers and a number K, check if there exist a pair of indices i,j s.t. a[i] + a[j] = K and i!=j.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines, first line of each test case contains N - size of the array and K, and the next line contains N integers - the elements of the array.

Constraints

30 points
1 <= T <= 100
2 <= N <= 1000

70 points
1 <= T <= 300
2 <= N <= 10000

General Constraints
-108 <= K <= 108
-108 <= ar[i] <= 108

Output Format

For each test case, print "True" if such a pair exists, "False" otherwise, separated by newline.

Sample Input 0

3
5 -15
-30 15 20 10 -10 
2 20
10 10 
4 7
-4 0 10 -7 
Sample Output 0

True
True
False



<======================================= C++ SOLUTION =================================>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void merge(int arr[],int low,int mid,int high){
    int tmp[high-low+1];
    int p1=low,p2=mid+1,k=0;
    while(p1<=mid && p2<=high){
        if(arr[p1]<arr[p2]){
            tmp[k++]=arr[p1++];
        }
        else{
            tmp[k++]=arr[p2++];
        }
    }
    while(p1<=mid){
        tmp[k++]=arr[p1++];
    }
    while(p2<=high){
        tmp[k++]=arr[p2++];
    }
    for(int i=0;i<high-low+1;i++){
        arr[low+i]=tmp[i];
    }
}
void mergesort(int arr[],int low,int high){
    if(low<high){
        int mid=(low+high)/2;
        mergesort(arr,low,mid);
        mergesort(arr,mid+1,high);
        merge(arr,low,mid,high);
    }
}
int pairs(int arr[],int n,int k){
    int i=0,j=n-1;
    while(i!=j){
        if(arr[i]+arr[j]==k){
            return 1;
            break;
        }
        else if(arr[i]+arr[j]>k){
            j--;
        }
        else{
            i++;
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
        mergesort(arr,0,n-1);
        if(pairs(arr,n,k)==1){
            printf("True\n");
    }
        else{
            printf("False\n");
        }
    }
    return 0;
}
