#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
void insertionsort(int arr[],int n){
    for(int i=1;i<n;i++){
        int x=arr[i];
        int idx=i-1;
        while(idx>=0 && arr[idx]>x){
            arr[idx+1]=arr[idx];
            idx--;
            
        }
        arr[idx+1]=x;
        printf("%d ",idx+1);
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
        insertionsort(arr,n);
        printf("\n");
    }
    return 0;
}
