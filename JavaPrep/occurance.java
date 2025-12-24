// Online Java Compiler
// Use this editor to write, compile and run your Java code online

import java.util.*;
class Main {
    public static void main(String[] args) {
        String str = "banana";
        char target = 'a';
        int count = 0;

       for(char ch:str.toCharArray()){
           if(ch==target){
               count++;
           }
       }
       System.out.println(count);
       
    }
    
    
}