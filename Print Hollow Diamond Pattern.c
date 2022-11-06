                                                      Print Hollow Diamond Pattern




#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int t;
    scanf("%d",&t);
    for(int r=1;r<=t;r++){
        printf("Case #%d:\n",r);
        int n;
        scanf("%d",&n);
        int r=n/2;
        for(int i=0;i<=r;i++){
            for(int j=0;j<=r-i-1;j++){
                printf(" ");
            }
            for(int k=0;k<=2*i;k++){
                if(k==0||k==2*i-1)
                    printf("* ");
                else
                    printf(" ");
            }
            printf("\n");
        }
        for(int i=1;i<=r;i++){
            for(int j=1;j<i+1;j++){
                printf(" ");
            }
            for(int k=1;k<=n-(2*i);k++){
                if(k==1||k==n-(2*i))
                    printf("*");
                else
                    printf(" ");
            }
            printf("\n");
        }
    }
    return 0;
}
