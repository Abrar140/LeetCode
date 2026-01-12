class Solution {
    public int maxPower(String s) {

        int max=1;
        int count=1;
        for(int i=0; i<s.length()-1;i++){
            if(s.charAt(i)!=s.charAt(i+1)){
                count=1;
            }else{
                count++;
                max=Math.max(count, max);
            }
        }

        return max;
        
    }
}