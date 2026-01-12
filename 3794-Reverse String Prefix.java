class Solution {
   
    public String reversePrefix(String s, int k) {

        StringBuilder str= new StringBuilder();
        for(char c: s.toCharArray()){
           str.append(c);
             k--;
             if(k==0){
                str.reverse();
            }

        }

        return str.toString();
        
    }
}