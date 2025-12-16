import java.util.*;

class Solution {
    public int uniqueMorseRepresentations(String[] words) {

        String[] morse= {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        
        Set<String> myset= new HashSet<>();
       
        for(String word:words){
            StringBuilder sb= new StringBuilder();
            for (char letter:word.toCharArray()){
                sb.append(morse[letter -'a']);   
            }
            myset.add(sb.toString());

        } 

        return myset.size();
        
    }
}