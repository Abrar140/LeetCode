class Solution {
    public int max(int[] g){
        int max=0;
        int index=0;
        for(int i=0; i<g.length; i++){
            if(g[i]>max){
                max=g[i];
                index=i;
            }
        }


        return index;
    }
    public long pickGifts(int[] gifts, int k) {
        while(k>0){
            int index=max(gifts);
             gifts[index]=(int) Math.floor(Math.sqrt(gifts[index]));
             k--;
        }

        long sum=0;
        for(int g:gifts){
            sum=sum+g;
        }
        return sum;
        
    }
}