class Solution {
    public boolean areOccurrencesEqual(String s) {
        int[]  arr= new int[26];
        int max= Integer.MIN_VALUE;

        for(char c: s.toCharArray()){
            arr[c-'a']++;
            max= Math.max(max , arr[c-'a'] );
        }


        for(int i: arr){
            if(i!=0 && i!=max ){
                return false;
            }
        }

        return true;
        

    }
}