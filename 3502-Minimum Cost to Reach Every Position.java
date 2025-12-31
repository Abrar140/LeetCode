class Solution {
    public int[] minCosts(int[] cost) {
        int minCost=cost[0];
        for(int i=1; i<cost.length; i++){
            minCost=Math.min(minCost,cost[i]);
            cost[i]=minCost;

            
        }

        return cost;
    }
}