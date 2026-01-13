class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int n=grid.length;
        int[] freq= new int[n*n];
        int repeated=0;
        int  missing=0;

        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[i].length; j++){
                freq[grid[i][j]-1]++;
            }
        }

       for(int i=0; i<freq.length; i++){
        if(freq[i]==0){
            missing=i+1;

        }else if(freq[i]==2){
            repeated=i+1;
        }
       }

       return new int[]{repeated, missing};

        
    }
}