class Solution {
    public void duplicateZeros(int[] arr) {
        
        int start=0;
        while(start<arr.length){
            if (arr[start]==0 && start+1<arr.length){
                    for(int j=arr.length-1; j>start+1; j--){
                          arr[j]= arr[j-1];

                    }
                   arr[start+1]=0;
                   start++;
                    
                }
            start++;

        }
        
    }
}