class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> map= new HashMap<>();
        for(int a:arr){
            map.put(a, map.getOrDefault(a,0)+1);
        }
        Set<Integer> set= new HashSet<>();
        for(int s:map.values()){
            if(set.contains(s)){
                return false;
            }
            set.add(s);
        }
        return true;
        
    }
}