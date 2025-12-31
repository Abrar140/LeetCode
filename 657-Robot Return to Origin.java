class Solution {
    public boolean judgeCircle(String moves) {
        int[] dir= new int[4];
        for(char letter: moves.toCharArray()){
            if(letter=='U'){
                dir[0]++;
            }else  if(letter=='D'){
                dir[1]++;
            } else  if(letter=='L'){
                dir[2]++;
            } else  if(letter=='R'){
                dir[3]++;
            }
        }

        return dir[0]==dir[1]&&dir[2]==dir[3];
        
    }
}