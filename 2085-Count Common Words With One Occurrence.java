import java.util.*;

class Solution {
    public int countWords(String[] words1, String[] words2) {
        Map<String, Integer> map1= new HashMap<>();
        Map<String, Integer> map2= new HashMap<>();

        for(String num: words1){
                map1.put(num, map1.getOrDefault(num,0)+1);       
        }
         for(String num: words2){
                map2.put(num, map2.getOrDefault(num,0)+1);       
        }
        int count=0;

        for (Map.Entry<String, Integer> entry: map1.entrySet()){
            if(entry.getValue()==1 && map2.containsKey(entry.getKey())){

             if(map2.get(entry.getKey())==1){
                count++;
             }
            }
            

        }

         

        return count;
        
    }
}