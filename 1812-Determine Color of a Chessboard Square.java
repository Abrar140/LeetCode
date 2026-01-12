class Solution {
    public boolean squareIsWhite(String coordinates) {

        int alpha= coordinates.charAt(0)-'a';
        int number= coordinates.charAt(1)-'0';

        if( alpha%2==0 && number%2==0 || alpha%2==1 && number%2==1 ){
            return true;
        }


        return false;

        
    }
}