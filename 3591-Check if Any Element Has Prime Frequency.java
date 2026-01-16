class Solution {
    public boolean isPrime(int n){
        if(n<2){
            return false;
        }

        for(int i=2; i*i<=n; i++){
          if(n%i==0){
            return false;
          }
        }

        return true;
    }
    public boolean checkPrimeFrequency(int[] nums) {
        int[] num= new int[101];

        for(int n:nums){
            num[n]++;
        }


        for(int n:num){
            if(n!=0){
                System.out.println("this is my number"+ n);

                if(isPrime(n)){
                return true;
                }
            }
        }


        return false;
        
    }
}