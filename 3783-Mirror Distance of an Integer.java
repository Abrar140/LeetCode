class Solution {
    public int mirrorDistance(int n) {
        int rev=n;
        int number =0;

        while(rev>0){
            int digit = rev % 10;
            number = number * 10 + digit;
            rev /= 10;

        }


        return Math.abs(number-n);
        
    }
}