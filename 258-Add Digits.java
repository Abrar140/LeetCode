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
    public int addDigits(int num) {

        while(num>9){
            num=digitSum(num);

        }
        return num;
        
    }
}