#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
void TOH(char src,char des,char temp,int n){
    
    if (n==0){
        return;
    }
    TOH(src,temp,des,n-1);
    printf("Move %d from %c to %c\n",n,src,des);
    TOH(temp,des,src,n-1);
}

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int t;
    scanf("%d",&t);
    while(t--){
        int n;
        scanf("%d",&n);
        char src='A',des='C',temp='B';
        long long res=pow(2,n)-1;
        printf("%lld\n",res);
        TOH(src,des,temp,n);
    }
    return 0;
}
