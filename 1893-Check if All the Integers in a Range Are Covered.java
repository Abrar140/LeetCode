class Solution {
    public boolean isCovered(int[][] ranges, int left, int right) {
      
      Set<Integer> set= new HashSet<>();
      for (int i=0; i<ranges.length; i++){
        int j= ranges[i][0];
        while(j<=ranges[i][1]){
            set.add(j);
            j++;

        }
        
      }

      while(left<=right){
        if (!set.contains(left)){
            return false;
        }
        left++;
      }

        return true;
    }
}