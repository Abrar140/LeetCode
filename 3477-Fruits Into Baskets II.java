import java.util.*;
class Solution {
    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        int count =fruits.length;
        List<Integer> list= new ArrayList<>();
        for (int bask:baskets){
            list.add(bask);
        }
        for(int fruit: fruits){
            for(int i=0; i<list.size(); i++){
                if(list.get(i)>= fruit){
                    count--;
                    list.remove(i);
                    break;
                }
            }
        }

        return count;
    }
}