// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.*;
class Main {
    public static void main(String[] args) {
        System.out.println("Try programiz.pro");
        int[] arr1= {0, 1, 0, 3, 12 ,12} ;
        int[] arr2= {0, 1, 0, 3, 12 ,5} ;
        Set<Integer> set= new HashSet<>();
        Set<Integer> common= new HashSet<>();

         for(int num:arr1){
             set.add(num);
        }
        
           for(int num:arr2){
             if(set.contains(num)){
                 common.add(num);
             }
        }
        
       
        

  
        for(int num:common){
        System.out.println(num);
        }
    }
}