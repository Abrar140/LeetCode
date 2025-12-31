class Solution {
    public int reverseDegree(String s) {
        int output=0;
        for(int i=0; i<s.length(); i++){

            output=output+((i+1)*('z'-s.charAt(i)+1));
            
        }

        return output;
        
    }
}