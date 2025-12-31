class Solution {
    public String largestOddNumber(String num) {

       int j=num.length()-1;
       while(j>=0){
            if(num.charAt(j)=='1' || num.charAt(j)=='3' ||num.charAt(j)=='5' ||num.charAt(j)=='7' ||num.charAt(j)=='9'  ){
            return num.substring(0,j+1);
        }
        j--;
       }

        return "";
        
    }
}