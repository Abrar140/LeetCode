// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.*;
class Main {
    public static void main(String[] args) {
        System.out.println("Try programiz.pro");
        int[]  arr=  {0, 1, 0, 3, 12};
        int index=0;
        for(int num:arr){
            if(num!=0){
                arr[index++]=num;
            }
        }
        while(index<arr.length){
            arr[index++]=0;
        }
        
        
        for(int num:arr){
            System.out.println(num);
        }
        
    }
}