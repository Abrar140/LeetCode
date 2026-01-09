class Solution {
    public int count(int n){
        if(n==0){
            return 1;
        }
        int count=0;
        if(n<0){
            count++;
            n=Math.abs(n);
        }
        while(n>0){
            n=n/10;
            count++;
        }
        return count;
    }
    public int[] findColumnWidth(int[][] grid) {

        int[] re= new int[grid[0].length];

        for(int i=0; i<grid[0].length ; i++){
            int max= Integer.MIN_VALUE;

                    for(int j=0; j<grid.length ; j++){
                        int count= count(grid[j][i]);
                        max=Math.max(count, max);
                    }
            re[i]=max;

        }

        return re;
        

    }
}