class Solution {
    public boolean isBalanced(String num) {
        int evenSum=0;
        int oddSum=0;
        for(int i=0; i<num.length() ; i++){
            int  a= num.charAt(i)-'0';
            if(i%2==0){
                evenSum=evenSum+a;

            }else{
                oddSum=oddSum+a;
            }
        }

        return evenSum==oddSum;
        
    }
}