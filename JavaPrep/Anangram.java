// Online Java Compiler
// Use this editor to write, compile and run your Java code online

import java.util.*;
class Main {
    public static void main(String[] args) {
        System.out.println("Try programiz.pro");
        System.out.println(anagram("listen", "silent"));
    }
    public static boolean anagram(String str, String str2){
        
        Map<Character, Integer> map= new HashMap<>();
        for(int i=0; i<str.length(); i++){
            map.put(str.charAt(i), map.getOrDefault(str.charAt(i),0)+1);
        }
        for(int i=0; i<str2.length(); i++){
            if(!map.containsKey(str2.charAt(i))){
                return false;
            }
            int  value=map.get(str2.charAt(i));
            value--;
            if(value==0){
                map.remove(str2.charAt(i));
            }else{
            map.put(str2.charAt(i),value);
            
            }
                
            
        }
        
        if(map.isEmpty()){
            return true;
        }
        return false;
    }
    
    
}