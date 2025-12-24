class Solution {
    public boolean canAliceWin(int[] nums) {
        int smaller=0;
        int greater=0;
        for(int num:nums){
            if(num>=10){
                greater=greater+num;
            }else{
                smaller=smaller+num;
            }
        }

        return greater== smaller? false:true;
        
    }
}