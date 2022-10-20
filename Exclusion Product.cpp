#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int n;
        scanf("%d",&n);
        long int k=1e9+7;
        int arr[n];
        for(int i=0;i<n;i++){
            scanf("%d",&arr[i]);
        }
        int prf[n];
        prf[0]=arr[0];
        for(int i=1;i<n;i++){
            prf[i]=((prf[i-1]%k)*(arr[i]%k))%k;
        }
        int srf[n];
        srf[n-1]=arr[n-1];
        for( int i=n-2;i>=0;i--){
            srf[i]=((srf[i+1]%k)*(arr[i]%k))%k;
        }
        int b[n];
        b[0]=srf[1];
        b[n-1]=prf[n-2];
        for( int i=1;i<=n-2;i++)
        {
            b[i]=((prf[i-1]%k)*(srf[i+1]%k))%k;
        }
        for( int i=0;i<n;i++)
        {
            printf("%d ",b[i]);
        }
        printf("\n");
    }
    return 0;
}
