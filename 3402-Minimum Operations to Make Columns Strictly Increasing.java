class Solution {
    public int minimumOperations(int[][] grid) {
        int operations=0;
    for(int j=0; j<grid[0].length; j++){
        for(int i=1; i<grid.length; i++){
            if(grid[i-1][j]>= grid[i][j]){
                int value= grid[i][j];
                grid[i][j]=grid[i-1][j]+1;
                operations= operations+grid[i][j]-value;

            }


            }
        }
        return operations;
        
    }
}