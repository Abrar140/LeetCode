class Solution {
    public boolean checkIfPangram(String sentence) {
        boolean[] alpha= new boolean[26];
        
        for(char s:sentence.toCharArray()){
            alpha[s-'a']=true;
        }
        for(boolean  b: alpha){
            if(b==false){
                return false;
            }
        }
      return true;
        
    }
}