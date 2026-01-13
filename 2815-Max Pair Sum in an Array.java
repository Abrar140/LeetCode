class Solution {
    public int maxnumber(int n){
        int max=-1;
        while(n>0){
            max=Math.max(max, n%10 );
            n=n/10;
        }
        return max;
    }
    public int maxSum(int[] nums) {

       int[][] top2= new int[10][2];
       for(int n: nums){
       int max= maxnumber(n);

       if(top2[max][0] <n){
        top2[max][1]=  top2[max][0];
        top2[max][0]=n;
       }else   if(top2[max][1]< n){
        top2[max][1]=n;
       }

       }
       int max=-1;

       for(int i=0; i<top2.length; i++){
        if(top2[i][0]!=0 && top2[i][1]!=0 ){
            max= Math.max(top2[i][0]+ top2[i][1] , max);
        }
       }

      

        return max;
        
    }
}