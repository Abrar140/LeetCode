class Solution {
    public int equalPairs(int[][] grid) {
        int n= grid.length;
        int output=0;
        Map<String, Integer> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < n; j++) {
                sb.append(grid[i][j]).append(",");
            }
            String row = sb.toString();
            map.put(row, map.getOrDefault(row, 0) + 1);
        }



        
        for(int i=0; i<n ; i++){
            StringBuilder sb = new StringBuilder();
            for(int j=0; j<n; j++){
                sb.append(grid[j][i]).append(",");
            }
           String col = sb.toString();
           if(map.containsKey(col)){
            output=output+ map.get(col);

           }


        }
      


        return output;
        
    }
}