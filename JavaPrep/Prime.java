// Online Java Compiler
// Use this editor to write, compile and run your Java code online

import java.util.*;
class Main {
    public static void main(String[] args) {
        System.out.println(isPrime(5));
    }
    public static boolean isPrime(int number){
        
        for(int i=2; i*i<=number;i++){
            if(number%i==0){
                return false;
            }
            
        }
      
                    return true;
    }
    
}