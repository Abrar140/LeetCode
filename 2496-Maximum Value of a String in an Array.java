class Solution {
    public int maximumValue(String[] strs) {
        int max=-1;
        for(String str:strs){
            boolean isDigit=true;
            for(int i=0; i<str.length(); i++){
                if(!Character.isDigit(str.charAt(i))){
                   isDigit=false;
                   break;
                }

            }
            if(isDigit){
                int value= Integer.parseInt(str);
                max=Math.max(max,value);
            }else{
                int value= str.length();
                max=Math.max(max,value);
            }

        }

        return max;
        
    }
}