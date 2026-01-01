class Solution {
    public int maximumNumberOfStringPairs(String[] words) {
       
        int output=0;
        Set<String> set= new HashSet<>();
        for(String w:words){
           StringBuilder str= new StringBuilder(w);
           String reversed=str.reverse().toString();

           if(set.contains(reversed)){
            output++;
           }else{
            set.add(w);
           }

        }
       
        return output;
        
    }
}




