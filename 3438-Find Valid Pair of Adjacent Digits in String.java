import java.util.*;

class Solution {
    public String findValidPair(String s) {
        int []   arr= new int[10];

        for(int i=0; i<s.length(); i++){
            int nums= s.charAt(i)- '0';
             arr[nums]++;
        }

      for(int i=0; i<s.length()-1; i++){
            int nums= s.charAt(i)- '0';
             int nums1= s.charAt(i+1)- '0';

            if(nums1!=nums && arr[nums]==nums && arr[nums1]==nums1){
                return  ""+nums+""+nums1;
            }
         
        }

        return "";
        
    }
}