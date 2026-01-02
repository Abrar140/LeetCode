class Solution {
    public double trimMean(int[] arr) {
      Arrays.sort(arr);
      int n= arr.length;
      int noofele= (5* n) / 100;
      int Sum=0;
      int count=0;
      for(int i=noofele; i<n-noofele; i++){
        Sum=Sum+arr[i];
        count++;
      }

      return  (double)Sum/count;
     
    }
}