class Solution {
    public int[] shortestToChar(String s, char c) {
        
        int[] output= new int[s.length()];
        for(int i=0; i<s.length(); i++){
           char n= s.charAt(i);
           if(n==c){
                        output[i]=0;
            continue;
           }
           int min= Integer.MAX_VALUE;
            for(int j=0; j<s.length(); j++){
               char m= s.charAt(j);
               if(m== c){
                 min=Math.min(min, Math.abs(i-j));
               }
            }
            output[i]=min;
        }



        return output;

    }
}