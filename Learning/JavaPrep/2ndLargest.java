// Online Java Compiler
// Use this editor to write, compile and run your Java code online

import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr={4,2,3,4,5};
        int max1=Integer.MIN_VALUE;
        int max2=Integer.MIN_VALUE;
        for (int num:arr){
            if (num>max1){
                max2=max1;
                max1=num;
            }else if(num>max2 && num<max1){
                max2=num;
                
            }
            
            
        }
      
       System.out.println(max2);
       
    }
    
    
}