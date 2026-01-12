class Solution {
    public boolean isEven(int a){
        return a%2==0;
    }
    public boolean checkTwoChessboards(String coordinate1, String coordinate2) {
        int alpha= coordinate1.charAt(0)-'a';
        int number= coordinate1.charAt(1)-'0';


        int alpha2= coordinate2.charAt(0)-'a';
        int number2= coordinate2.charAt(1)-'0';

        int color1=(alpha+number)%2;
        int color2=(alpha2+number2)%2;
  

     

        return color1==color2;
        
    }
}