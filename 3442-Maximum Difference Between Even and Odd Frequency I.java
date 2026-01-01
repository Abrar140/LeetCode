class Solution {
    public int maxDifference(String s) {
        Map<Character, Integer> map= new HashMap<>();
        for(char num: s.toCharArray()){
            map.put(num, map.getOrDefault(num,0)+1);

        }
        int mineven=Integer.MAX_VALUE;
        int maxodd=Integer.MIN_VALUE;
        for(int num:map.values()){
            if(num%2==0){
                mineven=Math.min(num, mineven);
            }else{
               maxodd=Math.max(num, maxodd);
            }
        }
       
        return maxodd-mineven;
        
    }
}
        
    