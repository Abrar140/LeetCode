// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.*;
class Main {
    public static void main(String[] args) {
        System.out.println("Try programiz.pro");
         String str = "sample string";
         Map<Character, Integer> map= new HashMap<>();
         for(char num:str.toCharArray()){
             if(num != ' '){
             map.put(num, map.getOrDefault(num,0)+1);
             }
         }
         
         char maxChar= '\0';
         int maxCount=0;
         for(Map.Entry<Character, Integer> entry: map.entrySet()){
             if(entry.getValue()>maxCount){
                 maxCount=entry.getValue();
                 maxChar=entry.getKey();
             }
         }
         

        System.out.println(maxChar + " "+ maxCount);
        
    }
}