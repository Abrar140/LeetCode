class Solution {
    public int[][] modifiedMatrix(int[][] matrix) {
        int[][] answer= matrix;
        int[] max = new int[matrix[0].length];


        for(int i=0; i<matrix[0].length; i++){
            for(int j=0; j<matrix.length; j++){
            max[i]= Math.max(max[i], matrix[j][i]);
            }
        }

          for(int i=0; i<answer.length; i++){
            for(int j=0; j<answer[i].length; j++){
                if(answer[i][j]==-1){
                  answer[i][j]=max[j];  
                }
            }
          }
        
        return answer;
        
    }
}