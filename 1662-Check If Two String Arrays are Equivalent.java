class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        StringBuilder str= new StringBuilder();
        StringBuilder strs=new StringBuilder();

        for(String s: word1){
            str.append(s);
        }

         for(String s: word2){
            strs.append(s);
        }
        

        return str.toString().equals(strs.toString());
        
    }
}