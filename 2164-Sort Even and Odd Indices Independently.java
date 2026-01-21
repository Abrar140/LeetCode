class Solution {
    public int[] sortEvenOdd(int[] nums) {
       int[] evenindex = new int[(nums.length + 1) / 2];
       int[] oddindex = new int[nums.length/2];
       int e=0;
       int o=0;
       for(int n=0; n<nums.length ; n++){
        if(n%2==0){
           evenindex[e]=nums[n];
           e++;
        }else{
            oddindex[o]=nums[n];
            o++;
        }
       }

       int [] result= new int[nums.length];
        Arrays.sort(evenindex);
        Arrays.sort(oddindex);
        e=0;
        o=oddindex.length-1;
        
        for(int i=0; i<result.length; i++){
             if(i%2==0){
                result[i]=evenindex[e];
                e++;

            }else{
                result[i]=oddindex[o];
                o--;
            }

        }
       
       
        return result;
        
    }
}