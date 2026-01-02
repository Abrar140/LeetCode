class Solution {
    public int heightChecker(int[] heights) {
        

        int[] arr= Arrays.copyOf(heights, heights.length);
         Arrays.sort(arr);
    
         int output=0;
         for(int i=0; i<heights.length; i++){
            if(arr[i]!=heights[i]){
                output++;
            }

         }

         return output;
    }
}