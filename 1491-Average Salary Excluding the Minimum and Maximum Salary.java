class Solution {
    public double average(int[] salary) {
        int totalSum=0;
        int min= Integer.MAX_VALUE;
        int max= Integer.MIN_VALUE;
        for(int num: salary){
            min=Math.min(num,min);
            max=Math.max(num,max);
            totalSum=totalSum+num;
        }
        totalSum=totalSum-min-max;

        return (double) totalSum/(salary.length-2);
    }
}