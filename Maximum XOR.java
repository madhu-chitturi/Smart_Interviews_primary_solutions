import java.io.*;
import java.util.*;
import java.lang.*;
class Node{
    Node[] c=new Node[2];
    Node(){
        c[0]=null;
        c[1]=null;
    }
}
public class Solution {
    public static int solve(int arr[],int n,int max){
        int bits=(int)(Math.log(max)/Math.log(2));
        Node root=new Node();
        for(int i=0;i<n;i++){
            insert(arr[i],root,bits);
        }
        int ans=0;
        for(int i=0;i<n;i++){
            ans=Math.max(query(root,arr[i],bits),ans);
        }
        return ans;
    }
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
        int ans=0;
        for(int i=bits;i>=0;i--){
            int idx=(x>>i)&1;
            if(root.c[1-idx]!=null){
                ans+=(1<<i);
                root=root.c[1-idx];
            }
            else{
                root=root.c[idx];
            }
        }
        return ans;
    }
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        int t=sc.nextInt();
        for(int i=0;i<t;i++){
            int n=sc.nextInt();
            int max=Integer.MIN_VALUE;
            int[] arr=new int[n];
            for(int j=0;j<n;j++){
                arr[j]=sc.nextInt();
                max=Math.max(max,arr[j]);
            }
            System.out.println(solve(arr,n,max));
        }
    }
}
