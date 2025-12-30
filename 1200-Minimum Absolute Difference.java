class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        List<List<Integer>> output= new ArrayList<>();
        Arrays.sort(arr);
        int mindifference=Integer.MAX_VALUE;

        for(int i=0; i<arr.length-1; i++){
            int diff= arr[i+1]- arr[i];
            if(diff<mindifference){
                mindifference=diff;
            }
        }

        
        for(int i=0; i<arr.length-1; i++){
            int diff= arr[i+1]- arr[i];
            if(diff==mindifference){
                List<Integer> list= new ArrayList<>();
                list.add(arr[i]);
                list.add(arr[i+1]);
                output.add(list);

            }
        }
   return output;
        
    }
}