import java.util.*;


class Solution {
    public int smallestAbsent(int[] nums) {
        Set<Integer>  numb = new HashSet<>();
        int  totalSum=0;
        
        for(int num: nums){
            numb.add(num);
            totalSum=totalSum+num;
        }
        int  average=((int)(totalSum/nums.length))+1;
        

        while(true){
            if(!numb.contains(average)&& average>0){

                 return average;
            }
                            average++;

        }


    }
}