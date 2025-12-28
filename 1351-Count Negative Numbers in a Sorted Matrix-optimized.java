class Solution {
    public int countNegatives(int[][] grid) {
        int count=0;
        int n=grid[0].length;
        int m=grid.length;
        int rows=0;
        int col=n-1;
        while(rows<m && col>=0){
            if(grid[rows][col]<0){
                count=count+(m-rows);
                col--;
            }else{
                rows++;
            }
        }
        
        return count;
        
    }
}