import java.io.*;
import java.util.*;
class Node{
    Node[] c=new Node[2];
    Node(){
        c[0]=null;
        c[1]=null;
    }
}
public class Solution {
    public static void insert(int x,Node root,int bits){
        for(int i=bits;i>=0;i--){
            int idx=(x>>i)&1;
            if(root.c[idx]==null){
                root.c[idx]=new Node();
            }
            root=root.c[idx];
        }  
    }
    public static int query(Node root,int x,int bits){
        int ans1=0;
        for(int i=bits;i>=0;i--){
            int idx=(x>>i)&1;
            if(root.c[1-idx]!=null){
                ans1+=(1<<i);
                root=root.c[1-idx];
            }
            else{
                root=root.c[idx];
            }
        }
        return ans1;
    }
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc =new Scanner(System.in);
        int t=sc.nextInt();
        for(int i=0;i<t;i++){
            int n=sc.nextInt();
            int[] arr=new int[n];
            int max=Integer.MIN_VALUE;
            for(int j=0;j<n;j++){
                arr[j]=sc.nextInt();
                max=Math.max(max,arr[j]);
            }
            int bits=(int)(Math.log(max)/Math.log(2));
            Node root=new Node();
            int a=0,ans=0;
            for(int k=0;k<n;k++){
                insert(a,root,bits);
                a=a^arr[k];
                ans=Math.max(query(root,a,bits),ans);
            }
            System.out.println(ans);
        }
    }
}
