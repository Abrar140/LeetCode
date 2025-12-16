class Solution {
    public int[] rowAndMaximumOnes(int[][] mat) {
       int index=0;
       int maximumcount1=0;
       int count=0;
       for(int rows=0; rows<mat.length;rows++){
        count=0;
        for(int columns=0; columns<mat[rows].length; columns++){
            if (mat[rows][columns]==1){
                count++;
            }
        }
        if (count>maximumcount1){
            maximumcount1=count;
            index=rows;
        }
       } 
       return new int[]{index, maximumcount1};
    }
}