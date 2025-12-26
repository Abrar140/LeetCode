class Solution {
    public int earliestTime(int[][] tasks) {
       
        int minfinish=Integer.MAX_VALUE;
        for(int i=0; i< tasks.length; i++){
            int finish= tasks[i][0]+ tasks[i][1];
            minfinish= Math.min(minfinish, finish);

        }

        return minfinish;
        
    }
}