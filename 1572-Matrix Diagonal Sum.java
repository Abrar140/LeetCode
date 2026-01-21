class Solution {
    public int diagonalSum(int[][] mat) {
        int Sum=0;
      

        for(int i=0; i<mat.length; i++){
            Sum= Sum+mat[i][i];
        }
          int i=0;
        int j=mat.length-1;
        while(j>=0){

            Sum= Sum+mat[i][j];
            i++;
            j--;
        }

        if(mat.length%2==1){
            int val= (mat.length-1)/2;
            Sum=Sum-mat[val][val];

        }

        return Sum;
        
    }
}