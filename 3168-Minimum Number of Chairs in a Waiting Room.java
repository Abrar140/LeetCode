class Solution {
    public int minimumChairs(String s) {
       
       int count=0;
                   int cnt=0;

        for(char c:s.toCharArray()){
            if(c=='E'){
                cnt++;
               count=Math.max(cnt, count);
            }else if(c=='L'){
                cnt--;
            }
        }

        return count;
        
    }
}