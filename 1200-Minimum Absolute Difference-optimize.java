class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        List<List<Integer>> output= new ArrayList<>();
        Arrays.sort(arr);
        int mindifference=Integer.MAX_VALUE;

        for(int i=0; i<arr.length-1; i++){
            int diff= arr[i+1]- arr[i];
            if(diff<mindifference){
                mindifference=diff;
                output.clear();
                output.add(Arrays.asList(arr[i],arr[i+1]));
            } else if(diff==mindifference){
                output.add(Arrays.asList(arr[i],arr[i+1]));

            }
        }

        
       
   return output;
        
    }
}