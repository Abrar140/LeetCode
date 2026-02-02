class Solution {
    public int findJudge(int n, int[][] trust) {
        Set<Integer> set = new HashSet<>();
        for(int i=0; i<trust.length ; i++){
            set.add(trust[i][0]);
        }
        int missing=0;
        for(int i=1; i<=n; i++){
            if(!set.contains(i)){
                missing=i;
                break;
            }
        }
        int count=0;
       for(int i=0; i<trust.length; i++){
        if((trust[i][1])==missing){
            count++;
        }
     
       }
       
       return count==n-1? missing: -1;
        
    }
}