class Solution {
    public int digitofSum(int n){
        int sum=0;
        while(n>0){
            sum=sum+n%10;
            n=n/10;
            
        }
        return sum;

    }
    public int countBalls(int lowLimit, int highLimit) {
        int[] arr= new int[46];
        for(int i=lowLimit; i<highLimit+1; i++){

            arr[digitofSum(i)]++;
        }
int max=0;
        for(int n: arr){
         max=Math.max(max, n);
        }


return max;
    }
}