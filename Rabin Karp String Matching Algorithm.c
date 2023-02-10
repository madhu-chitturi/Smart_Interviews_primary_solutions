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
    while(t--){
        string a,b;
        cin >>b>>a;
        int p=97,pow1=p,hashA=0,hashB=0,i=0,cnt=0;
        for(i=0;i<b.length();i++){
            hashA+=a[i]*pow1;
            hashB+=b[i]*pow1;
            pow1=pow1*p;
        }
        if(hashA==hashB){
            cnt++;
        }
        int j=0,prevp=p;
        while(i<a.length()){
            hashA+=a[i++]*pow1;
            hashA-=a[j++]*prevp;
            pow1=pow1*p;
            prevp=prevp*p;
            hashB=hashB*p;
            if(hashA==hashB){
             cnt++;
            }
        }
    printf("%d\n",cnt);
    }
    return 0;
}
