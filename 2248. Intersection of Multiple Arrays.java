class Solution {
    public List<Integer> intersection(int[][] nums) {
        Map<Integer, Integer> map = new HashMap<>();

       for(int [] n:nums){
        for(int digit: n){
            map.put(digit, map.getOrDefault(digit,0)+1);
        }
       }
       List<Integer> list= new ArrayList<>();
       for(Map.Entry<Integer, Integer> entry: map.entrySet()){
           if(entry.getValue()==nums.length){
            list.add(entry.getKey());

           }
       }

       Collections.sort(list);
       return list;

               
    }
}