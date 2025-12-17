class Solution {
    public int[] decrypt(int[] code, int k) {
    
    int[] mycode= new int[code.length];
    int windowSum=0;
    int n=code.length;
    if(k>0){
       for(int i=1; i<=k;i++){
        windowSum=windowSum+code[i%n];
       }
        for(int i=0; i<code.length;i++){
            mycode[i]=windowSum;
            windowSum=windowSum-code[(i+1)%n]+code[(i+k+1)%n];         
        }
    }
    else if(k<0){
        k=-k;
       for(int i=1; i<=k;i++){
        windowSum=windowSum+code[(n-i)%n];
       }
        for(int i=0; i<code.length;i++){
            mycode[i]=windowSum;
            // windowSum=windowSum-code[(n-i-1)%n]+code[(n-i-1-k+n)%n]; 
           windowSum = windowSum - code[(n + i - k) % n] + code[i % n];


        }
    }

    return mycode;    
    }
}