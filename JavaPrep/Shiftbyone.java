// Online Java Compiler
// Use this editor to write, compile and run your Java code online

import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = { 0, 1, 2, -3, 15 };
        int first= arr[0];
         for (int i=0; i<arr.length-1; i++){
             arr[i]=arr[i+1];
         }
         arr[arr.length-1]=first;
        
     


      for (int num :arr){
       System.out.println(num);
      }
    }
    
    
}
