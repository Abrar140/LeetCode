// Online Java Compiler
// Use this editor to write, compile and run your Java code online

import java.util.*;
class Main {
    public static void main(String[] args) {
        
        int num=10234;
        int sum=0;

        while(num>=10){
            sum=sum+num%10;
            
            num=num/10;
            
        }
        sum=sum+num;
        
      
        System.out.println(sum);
    }
    
    
}