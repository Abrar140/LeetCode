class Solution {
    public void duplicateZeros(int[] arr) {
        
        int zero=0;
        int n= arr.length;
        for(int num:arr){
            if(num==0){
                zero++;
            }
        }
        System.out.println("this is my count of zeros"+zero);
       
       int i=n-1;
       int j=n+zero-1;
       while(i<j){
        if(j<n){
            arr[j]=arr[i];
        }
        if(arr[i]==0){
            j--;
            if(j<n){
                arr[j]=0;
            }

        }
        i--;
        j--;
        
       }

          
        
    }
}