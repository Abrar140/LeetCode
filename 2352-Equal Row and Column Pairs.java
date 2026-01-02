class Solution {
    public int equalPairs(int[][] grid) {
        int n= grid.length;
        String[] rows= new String[n];
        String[] columns= new String[n];
        int output=0;
        
        for(int i=0; i<n ; i++){
            StringBuilder r= new StringBuilder();
            StringBuilder c= new StringBuilder();
            for(int j=0; j<n; j++){

                r.append(grid[i][j]).append(",");
                c.append(grid[j][i]).append(",");


            }
            rows[i]=r.toString();
            columns[i]=c.toString();

        }
        for(String r:rows){
            System.out.println(r);
        }


        for(String r:rows){
            for(String c:columns){
                if(r.equals(c)){
                 output++;
                }
            }
        }


        return output;
        
    }
}