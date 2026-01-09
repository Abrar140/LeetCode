class Solution {
    public int countPoints(String rings) {
        int[] red= new int[10];
        int[] blue= new int[10];
        int[] green= new int[10];
        int n=rings.length()-1;
        while(n>0){
            char rod= rings.charAt(n);
            char color= rings.charAt(n-1);
            n-=2;
            if(color=='R'){
                red[rod-'0']++;
            }else if(color=='G'){
                green[rod-'0']++;
            }else if(color=='B'){
                blue[rod-'0']++;
            }

        }
        int count=0;
        for(int i=0; i<10; i++){

            if(red[i]>0 && green[i]>0 && blue[i]>0){
                count++;
            }

        }

        return count;
    }
}