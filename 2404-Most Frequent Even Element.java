import java.util.*;
class Solution {
    public int mostFrequentEven(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int minvalue=-1;
        int maxcount=0;
        for(int num: nums){
            if(num%2==0){
                map.put(num,map.getOrDefault(num,0)+1);

                   if(maxcount< map.get(num)){
                minvalue=num;
                maxcount=map.get(num);
            }else    if(maxcount==map.get(num) && minvalue >num ){
                minvalue=num;
                maxcount=map.get(num);
            }
            }
         
        }
        return minvalue;

        
    }
}