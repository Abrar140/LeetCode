class Solution {
    public List<Integer> lastVisitedIntegers(int[] nums) {
        
        List<Integer>  seen= new  ArrayList<>();
        List<Integer>  ans= new  ArrayList<>();
        
        int k=0;
        for(int num: nums){
            if(num>0){
                seen.add(0, num);
                k=0;
            }
            if(num==-1){
                if(k>=seen.size()){
                    ans.add(num);
                }else{
              ans.add(seen.get(k));
                k++;
                }
              
            }
        }

        System.out.println(seen);
        return ans;
    }
}