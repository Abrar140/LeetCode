// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.*;
class Main {
    public static void main(String[] args) {
        System.out.println("Try programiz.pro");
        int[] arr= {1,2,3,5} ;
        int n= arr.length+1;
        int Sum= (n*(n+1))/2;

         for(int num:arr){
             Sum=Sum-num;
             
        }

        System.out.println(Sum);
        
    }
}