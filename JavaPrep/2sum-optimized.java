// Online Java Compiler
// Use this editor to write, compile and run your Java code online

import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = { 0, -1, 2, -3, 1 };
        int target=-2;
        boolean found=false;
        Set<Integer> set= new HashSet<>();
         
         for (int num: arr){
             if(set.contains(target-num)){
                 found=true;
             }
             set.add(num);
         }
        
     


      
       System.out.println(found);
       
    }
    
    
}