class Solution {
    public String firstPalindrome(String[] words) {
        for(String word:words){
            int left=0;
            int right=word.length()-1;
            boolean notFound=false;
                while(left<right){
                    if (word.charAt(left)==word.charAt(right)){
                        left++;
                        right--;
                    }
                    else{
                        notFound=true;
                        break;
                    }
                }

            
            if(!notFound){
                return word;
            }
        }

        return "";
        
    }
}