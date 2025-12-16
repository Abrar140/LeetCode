import java.util.*;

class Solution {
    public int[] recoverOrder(int[] order, int[] friends) {

        Set<Integer> friendSet= new HashSet<>();
        for(int friend:friends){
            friendSet.add(friend);
        }
        
        int finish[]=new int[friends.length];
        int count=0;
        for (int o: order ){
          if(friendSet.contains(o)){
            finish[count++]=o;
          }
        }
        return finish;

    }
}