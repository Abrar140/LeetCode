import java.util.*;
class Solution {

    public int findShortestSubArray(int[] nums) {
       

        Map<Integer, Integer> map= new HashMap<>();
        Map<Integer, Integer> first= new HashMap<>();
         Map<Integer, Integer> last= new HashMap<>();


        for(int i=0; i<nums.length; i++){
            if(!first.containsKey(nums[i])){
                first.put(nums[i], i);

            }
            map.put(nums[i], map.getOrDefault(nums[i], 0)+1);
           
        }
         for(int i=nums.length-1; i>=0; i--){
            if(!last.containsKey(nums[i])){
                last.put(nums[i], i);

            }
           
        }

         int max=0;
        int maxnumber=0;
        int smallestone=Integer.MAX_VALUE;

        for(Map.Entry<Integer, Integer> entry: map.entrySet()){
            int smallest = last.get(entry.getKey()) - first.get(entry.getKey()) + 1;
            if (entry.getValue() > max ||(entry.getValue() == max && smallest < smallestone)) {               max=entry.getValue();
                maxnumber= entry.getKey();
                smallestone= smallest;
            }

        }



        System.out.println(map + " "+ first+ " "+last);

        return smallestone;
        
    }
}