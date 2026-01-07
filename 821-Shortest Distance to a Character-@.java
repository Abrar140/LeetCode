class Solution {
    public int[] shortestToChar(String s, char c) {
        
        int[] output= new int[s.length()];
         int m= s.length();
         int prev=-m;

        for(int i=0; i<m; i++){
           char n= s.charAt(i);
           if(n==c){
            prev=i;
           }
           output[i]= i-prev;
        }
        prev= 2 * m;
        
         for(int j=m-1; j>=0; j--){
               char z= s.charAt(j);
               if(z== c){
                prev=j;
               }

            output[j]=Math.min(output[j], prev-j);

            }
        



        return output;

    }
}