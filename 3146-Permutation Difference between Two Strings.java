class Solution {
    public int findPermutationDifference(String s, String t) {
        Map<Character, Integer> map= new HashMap<>();
        int Sum=0;
        for(int i=0; i<t.length(); i++){
            map.put(t.charAt(i), i);
        }
        

        for(int i=0; i<s.length(); i++){
            Sum= Sum+Math.abs(map.get(s.charAt(i))-i);

        }
        
        return Sum;
    }
}