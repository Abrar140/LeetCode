class Solution {
    public char slowestKey(int[] releaseTimes, String keysPressed) {
        int[] alpha= new int[26];
        int prev=0;
        int max=Integer.MIN_VALUE;
        for(int i=0; i<releaseTimes.length; i++){
            char c= keysPressed.charAt(i);
            int  a= releaseTimes[i]-prev;
            prev=releaseTimes[i];
            max=Math.max(a,max);
            alpha[c-'a']= Math.max(a, alpha[c-'a']);
        }

            for(int i=alpha.length-1; i>=0; i--){
                if(max==alpha[i]){
                    char c= (char) (i+'a');

                    return c;
                }
 
        }
        return  ' ';
        
    }
}