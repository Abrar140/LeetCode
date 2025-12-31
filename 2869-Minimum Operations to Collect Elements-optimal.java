import java.util.*;

class Solution {
    public int minOperations(List<Integer> nums, int k) {
       boolean[] seen= new boolean[k+1];
       int count=0;
       int remaining=k;

        for (int i = nums.size()-1; i >= 0 && remaining>0; i--) {
            int num= nums.get(i);
            count++;


            if(num<=k && !seen[num]){
                seen[num]=true;
                remaining--;
            }

        }

      

        return count;
    }
}
