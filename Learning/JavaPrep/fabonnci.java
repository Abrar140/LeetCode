// Online Java Compiler
// Use this editor to write, compile and run your Java code online

import java.util.*;
class Main {
    public static void main(String[] args) {
        int num=5;
        int one=0;
        int two=1;
        System.out.print(""+one+""+two);
        for(int i=2; i<num; i++){
            int now=one+two;
            System.out.print(""+now);
            one=two;
            two=now;

            
            
        }
        
       
        
       
    }
    
    
}