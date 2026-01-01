class Solution {
    public boolean digitCount(String num) {
        int[] freq= new int[10];
        
        for(char n:num.toCharArray()){
            freq[n-'0']++;
        }

    
        for(int j=0; j<num.length(); j++){
            int digit = num.charAt(j)-'0';
            if( freq[j]!=digit){
                return false;
            }
        }


        return true;

    }
}