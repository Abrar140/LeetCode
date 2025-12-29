class Solution {
    public int getLeastFrequentDigit(int n) {
        int[]  freq =new int[10];
        int smallindex=Integer.MAX_VALUE;
        int min=Integer.MAX_VALUE;

        while(n>0){
            int num= n%10;
            freq[num]++;
            n=n/10;

            }

    

        for(int i=0; i<freq.length; i++){
            if(freq[i]==0){
                continue;
            }
            if (freq[i]<min){
                min=freq[i];
                smallindex=i;

            }else if(freq[i]==min && smallindex>i){
                 min=freq[i];
                smallindex=i;

            }
        }

        return  smallindex;

        
    }
}