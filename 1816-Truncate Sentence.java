class Solution {
    public String truncateSentence(String s, int k) {
        int count=0;
        String returning="";
        for (int i=0; i<s.length();i++){
            if (count==k){
                returning= s.substring(0,i-1);
                break;
            }
            if(s.charAt(i)== ' '){
                count=count+1;
            }
            if(i==s.length()-1 && count==k-1){
                returning=s;
            }
        }

        return returning;
        
    }
}