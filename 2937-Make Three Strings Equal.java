class Solution {
    public int findMinimumOperations(String s1, String s2, String s3) {
        int st1=s1.length();
        int st2=s2.length();
        int st3=s3.length();

       int minlength=Integer.MAX_VALUE;
        minlength= Math.min(minlength, st1);
        minlength= Math.min(minlength, st2);
        minlength= Math.min(minlength, st3);
        int count=0;

        for(int i=0; i< minlength; i++){
            if(s1.charAt(i)!=s2.charAt(i) || s3.charAt(i)!=s2.charAt(i)   || s3.charAt(i)!=s1.charAt(i)){
                if(i==0){
                    return -1;
                }
                break;
            }
            count++;
        }



     return st1-count+ st2-count+st3-count;

        
    }
}