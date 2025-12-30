class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int [] output= new int[nums1.length];
        for(int i=0; i<nums1.length; i++){
            boolean check=false;
            int max=-1;
            for(int j=0; j< nums2.length ; j++){
                if(nums1[i]==nums2[j]){
                    check=true;
                }
                if(check && nums1[i]<nums2[j] ){
                max=nums2[j];
                break;
                }

            }
            output[i]=max;
        }
        return output;
    }
}