class Solution {
     public int digitSum(int n){
        int Sum=0;
        n = Math.abs(n);
        while(n>0){
            Sum= Sum+ n%10;
            n=n/10;

        }
        return Sum;
    }
    public int getLucky(String s, int k) {
        int Sum=0;
        for(char c:s.toCharArray()){
         Sum=Sum+digitSum(c-'a'+1);
        }
        for(int i=1; i<k ; i++){
            Sum=digitSum(Sum);
        }
        return Sum;
    }
}