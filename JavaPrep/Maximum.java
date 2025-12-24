// Online Java Compiler
// Use this editor to write, compile and run your Java code online

import java.util.*;
class Main {
    public static void main(String[] args) {
        
        int[] array= {1,12,3,4,5,6};
        int max=array[0];
        for(int arr:array){
            if(max<arr){
                max=arr;
            }
        }
        System.out.println(max);
    }
    
    
}