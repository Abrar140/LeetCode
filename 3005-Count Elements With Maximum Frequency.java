import java.util.*;

class Solution {
    public int maxFrequencyElements(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int maxaccurance=0;
        int count=0;
        for(int num:nums){
            map.put(num, map.getOrDefault(num,0)+1);
            if(map.get(num)>maxaccurance){
                maxaccurance= map.get(num);
            }
        }
        
        for(int entry:map.values()){
            if(entry==maxaccurance){
                count++;
            }
        }

        return maxaccurance*count;

        
    }
}