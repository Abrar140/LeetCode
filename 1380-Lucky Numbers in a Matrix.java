import java.util.*;

class Solution {
    public List<Integer> luckyNumbers(int[][] matrix) {
    
     int[] maxcol= new int[matrix[0].length];
     int  index=0;
     List<Integer> list= new ArrayList<>();
     
     for(int i=0; i<matrix[0].length; i++){
        int  max= Integer.MIN_VALUE;
        for(int j=0; j<matrix.length; j++){
            
            max=Math.max(max, matrix[j][i]);    
     }
     maxcol[index++]=max;
     }


      for(int i=0; i<matrix.length; i++){
        int  min= Integer.MAX_VALUE;
        int colIndex = -1;


        for(int j=0; j<matrix[0].length; j++){
            
  if (matrix[i][j] < min) {
                    min = matrix[i][j];
                    colIndex = j;
                }     }

         if(min==maxcol[colIndex]){
            list.add(min);

         }
     }

        return list;

    }
}