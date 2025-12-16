import java.util.*;

class Solution {
    public int uniqueMorseRepresentations(String[] words) {

        String alphabets[]= {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        
        Set<String> myset= new HashSet<>();
       
        for(String word:words){
            String transform="";
            for (char letter:word.toCharArray()){
                transform= transform+ alphabets[(int)letter-97];   
            }
            myset.add(transform);

        } 

        return myset.size();
        
    }
}