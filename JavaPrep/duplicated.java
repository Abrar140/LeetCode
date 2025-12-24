// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.*;
class Main {
    public static void main(String[] args) {
        System.out.println("Try programiz.pro");
        int[] arr1= {0, 1, 0, 3, 12 ,12} ;
        Set<Integer> set= new HashSet<>();
        Set<Integer> duplicate= new HashSet<>();

         for(int num:arr1){
             if(set.contains(num)){
                 duplicate.add(num);
             }
             else{
                 set.add(num);
             }
        }
        
        
       
        

  
        for(int num:duplicate){
        System.out.println(num);
        }
    }
}