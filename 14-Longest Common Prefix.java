class Solution {
    public String longestCommonPrefix(String[] strs) {
        String word=strs[0];
        for(String letter:strs){
            if(letter.length()<word.length()){
                word=letter;
            }
        }
         for(String str:strs){
            int i=0;
            for( ; i<str.length() && i<word.length();){
             if(word.charAt(i)!=str.charAt(i)){
               break;
             }
             i++;
            }
             word = word.substring(0, i);

             if (word.isEmpty()){
                break;
             }


           
        }


        
        return word;
    }
}