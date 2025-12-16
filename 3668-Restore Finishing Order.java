class Solution {
    public int[] recoverOrder(int[] order, int[] friends) {
        
        int finish[]=new int[friends.length];
        int count=0;
        for (int each: order ){
            for (int friend: friends){
                if(each==friend){
                    finish[count]=each;
                    count++;
                }
            }
        }
        return finish;

    }
}