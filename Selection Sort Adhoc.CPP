#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std; 
void selection(int arr[], int n)  
{    
    for (int i = 0; i < n-1; i++)     
    {  
        int small = 0;   
        for (int j = 1; j < n-i; j++){ 
            if (arr[j] > arr[small])  
                small = j;     
        }
        printf("%d ",small);
        int temp = arr[small];  
        arr[small] = arr[n-1-i];  
        arr[n-1-i] = temp;  
        
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
        selection(arr,n);
        printf("\n");  
    }
    return 0;
}
