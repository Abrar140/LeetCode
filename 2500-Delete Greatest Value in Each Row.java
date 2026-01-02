import java.util.*;

class Solution {
    public int deleteGreatestValue(int[][] grid) {
        
         for(int []  r : grid){
        Arrays.sort(r);

     }

    int output=0;
     for(int i=grid[0].length-1; i>=0; i--){
         int max= Integer.MIN_VALUE;

             for(int j=grid.length-1; j>=0; j--){
                if(max<grid[j][i]){
                    max=grid[j][i];
                }



             }
             output=output+max;

     }

    
     return output;
        
    }
}