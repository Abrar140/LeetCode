class Solution {
    public String bestHand(int[] ranks, char[] suits) {
        
        int[] alpha= new int[4];
        for(char r:suits){
            alpha[r-'a']++;
        }
        for(int a: alpha){
            if(a==5){
                return "Flush";
            }
        }
        int [] rank= new int[13];
        for(int r:ranks){
            rank[r-1]++;
        }

        for(int r:rank){
          if(r>=3){
                return "Three of a Kind";
            }       
            
         }


             for(int r:rank){
          if(r>=2){
                return "Pair";
            }       
            
         }



   return "High Card";

    }
}