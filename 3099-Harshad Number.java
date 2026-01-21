class Solution {
    public int sumOfTheDigitsOfHarshadNumber(int x) {

        int Sum=0;
        int xs=x;
        while(xs>0){
            Sum=Sum+ (xs%10);
            xs=xs/10;
        }

        if(x%Sum==0){
            return Sum;
        }
        return -1;
        
    }
}1572. Matrix Diagonal Sum