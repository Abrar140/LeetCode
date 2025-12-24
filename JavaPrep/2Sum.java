// Online Java Compiler
// Use this editor to write, compile and run your Java code online

import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = { 0, -1, 2, -3, 1 };
        int target = -2;
        boolean found=false;
        Arrays.sort(arr);
        int left=0;
        int right=arr.length-1;
        while(left<right){
            int value =arr[left]+arr[right];
            if(value==target){
                found=true;
                break;
            }else if(value>target){
                right--;
            }else{
            left++;
            }
        }
     


      
       System.out.println(found);
       
    }
    
    
}