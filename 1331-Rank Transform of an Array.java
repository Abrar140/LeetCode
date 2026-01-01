class Solution {
    public int[] arrayRankTransform(int[] arr) {
        
        Set<Integer> set= new TreeSet<>();
        Map<Integer, Integer>map=  new HashMap<>();

        for(int a:arr){
            set.add(a);
        }
        int i=1;
        for(int s:set){
        map.put(s,i);
        i++;

        }

        for(int j=0; j<arr.length; j++){
            arr[j]=map.get(arr[j]);
        }

        return  arr;
    }
}