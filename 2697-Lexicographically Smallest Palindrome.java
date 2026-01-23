class Solution {
    public String makeSmallestPalindrome(String s) {
        int left=0;
        int right=s.length()-1;
        char [] c= new char[right+1];
        while(left<=right){
            char l= s.charAt(left);
            char r=s.charAt(right);
            if(l>r){
                l=r;
            } else  if(l<r){
              r=l;
            }
            c[left]=l;
            c[right]=r;
            left++;
            right--;


        }

        return  new String(c);
        
    }
}