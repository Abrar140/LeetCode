class Solution {
    public int minDeletion(String s, int k) {
        int[] alpha= new int[26];
        for(char n: s.toCharArray()){
            alpha[n-'a']++;
        }
        int output=0;
        Arrays.sort(alpha);
        for(int i=0; i<alpha.length-k ; i++){
            output=output+alpha[i];

        }

        return output;
    }
}