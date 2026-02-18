// Online Java Compiler
// Use this editor to write, compile and run your Java code online

import java.util.*;
class Main {
    public static void main(String[] args) {
        System.out.println(vowels("Jello"));
    }
    public static int  vowels(String str){
        String string= str.toLowerCase();
        int count=0;
        for(char ch:string.toCharArray()){
            if(ch =='a'|| ch =='e' || ch =='i'|| ch =='o'|| ch =='u'){
                count++;
            }
        }
        return count;
        

    }
    
}