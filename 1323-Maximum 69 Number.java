class Solution {
    public int maximum69Number (int num) {

        int number=0;
        int nums=num;
         while (nums>0){
            int n= nums%10;
            number=number*10+n;
            nums=nums/10;   
         }
        nums=0;
        
        boolean flag=true;
         while (number>0){
            int n= number%10;
            if( flag &&n==6){
                nums=nums*10+9;
                flag=false;
            }else{
               nums=nums*10+n;
            }

            number=number/10;
            
         }
        
        return nums;
    }
}