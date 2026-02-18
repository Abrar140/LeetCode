// Online Java Compiler
// Use this editor to write, compile and run your Java code online

import java.util.*;
class Main {
    public static void main(String[] args) {
        System.out.println("Try programiz.pro");
        System.out.println(anagram("listen", "sileit"));
    }
    public static boolean anagram(String str, String str2){
        if(str.length()!=str2.length()){
            return false;
        }
        char[] s1=str.toCharArray();
        char[] s2=str2.toCharArray();
        
        Arrays.sort(s1);
        Arrays.sort(s2);
        
        return Arrays.equals(s1,s2);
        
    }
    
}