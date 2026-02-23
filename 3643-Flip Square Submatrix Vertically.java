class Solution {
    public int[][] reverseSubmatrix(int[][] grid, int x, int y, int k) {

        int rowStart = x;
        int rowEnd = x + k - 1;
        int colStart = y;
        int colEnd = y + k - 1;

        while (rowStart < rowEnd) {
            for (int col = colStart; col <= colEnd; col++) {
                int temp = grid[rowStart][col];
                grid[rowStart][col] = grid[rowEnd][col];
                grid[rowEnd][col] = temp;
            }
            rowStart++;
            rowEnd--;
        }

        return grid;
    }
}