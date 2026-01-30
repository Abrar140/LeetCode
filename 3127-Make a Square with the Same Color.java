class Solution {
    public boolean canMakeSquare(char[][] grid) {
        boolean re=false;

        char cell1 = grid[0][0];
char cell2 = grid[0][1];
char cell3 = grid[0][2];
char cell4 = grid[1][0];
char cell5 = grid[1][1];
char cell6 = grid[1][2];
char cell7 = grid[2][0];
char cell8 = grid[2][1];
char cell9 = grid[2][2];

if (
    (cell1 == cell2 && cell1 == cell4 && cell1 == cell5) ||
    (cell2 == cell3 && cell2 == cell5 && cell2 == cell6) ||
    (cell4 == cell5 && cell4 == cell7 && cell4 == cell8) ||
    (cell5 == cell6 && cell5 == cell8 && cell5 == cell9)
) {
    re = true;
}



if (
    (cell1 == cell2 && cell1 == cell4) || (cell1 == cell2 && cell1 == cell5) || (cell1 == cell4 && cell1 == cell5) || (cell2 == cell4 && cell2 == cell5) ||
    (cell2 == cell3 && cell2 == cell5) || (cell2 == cell3 && cell2 == cell6) || (cell2 == cell5 && cell2 == cell6) || (cell3 == cell5 && cell3 == cell6) ||
    (cell4 == cell5 && cell4 == cell7) || (cell4 == cell5 && cell4 == cell8) || (cell4 == cell7 && cell4 == cell8) || (cell5 == cell7 && cell5 == cell8) ||
    (cell5 == cell6 && cell5 == cell8) || (cell5 == cell6 && cell5 == cell9) || (cell5 == cell8 && cell5 == cell9) || (cell6 == cell8 && cell6 == cell9)
) {
    re = true;
}
        return re;
        
    }
}