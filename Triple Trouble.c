                                                                          Triple Trouble

Given an array of size 3X+1, where every element occurs three times, except one element, which occurs only once. Find the element that occurs only once.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N - the size of the array (of the form 3X + 1) and second line contains the elements of the array.

Constraints

1 <= T <= 300
1 <= N <= 104
1 <= A[i] <= 109

Output Format

For each test case, print the number which occurs only once, separated by new line.

Sample Input 0

2
10
5 7 8 7 7 5 5 9 8 8 
7
10 20 20 30 20 10 10 
Sample Output 0

9
30

<================================ C SOLUTION ========================================>

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
void Merge(int arr[],int low,int mid,int high){
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
    while(p2<=high){
    tmp[k++]=arr[p2++];
}
    while(p1<=mid){
        tmp[k++]=arr[p1++];
    }
        for(int i=0;i<high-low+1;i++){
        arr[low+i]=tmp[i];
    }
}
void ms(int arr[],int low,int high){
        if(low<high){
            int mid=(low+high)/2;
            ms(arr,low,mid);
            ms(arr,mid+1,high);
        Merge(arr,low,mid,high);
    }
}
int main() {
    int t;
    scanf("%d",&t);
    while(t--){
        int n;
        scanf("%d",&n);
        int low=0,high=n-1;
        int arr[n];
        for(int i=0;i<n;i++){
            scanf("%d",&arr[i]);
        }
        ms(arr,low,high);
        for(int i=0;i<=n-1;i++){
                if(arr[i]!=arr[i+1] && arr[i]!=arr[i-1])
                {
                    printf("%d\n",arr[i]);
                }
        }
    }

    return 0;
}
