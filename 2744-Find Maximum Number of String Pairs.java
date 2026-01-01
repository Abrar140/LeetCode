class Solution {
    public int maximumNumberOfStringPairs(String[] words) {

        int output=0;
        for(int i=0; i<words.length-1; i++){
             for(int j=i+1; j<words.length; j++){
                StringBuilder str= new StringBuilder(words[j]);
                if(words[i].equals( str.reverse().toString())){
                    output++;
                }
        }
        }
        return output;
        
    }
}