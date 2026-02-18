// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.*;
class Main {
    public static void main(String[] args) {
        System.out.println("Try programiz.pro");
        int[]  arr1=  {0, 1, 0, 3, 12};
        int[]  arr2={10,5,4,2,11};
        int[]  result= new int[arr1.length+arr2.length];
        int first=0;
        int second=0;
        int third=0;
        
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        
        while(first<arr1.length &&second<arr2.length){
            if(arr1[first]>=arr2[second]){
                result[third++]=arr2[second];
                second++;
            }else {
                result[third++]=arr1[first];
                first++;}
        }
        
         while(first<arr1.length ){
            
                result[third++]=arr1[first];
                first++;
        }
          while(second<arr2.length ){
            
                result[third++]=arr2[second];
                second++;
        }
        

        
        
        for(int num:result){
            System.out.println(num);
        }
        
    }
}