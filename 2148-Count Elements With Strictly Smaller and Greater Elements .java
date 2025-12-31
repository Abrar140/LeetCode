class Solution {
    public int countElements(int[] nums) {

        int minvalue=Integer.MAX_VALUE;
        int mincount=0;
        int maxvalue=Integer.MIN_VALUE;
        int maxcount=0;
        for(int num:nums){
            if(num>maxvalue){
                maxvalue=num;
                maxcount=0;
            }
            if(num==maxvalue){
               maxcount++;
            }

              if(num<minvalue){
                minvalue=num;
                mincount=0;
            }
            if(num==minvalue){
               mincount++;
            }
        }
        int answer=nums.length-mincount-maxcount;

        return answer>0?answer:0;
        
    }
}