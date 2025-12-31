class Solution {
    public List<List<Integer>> largeGroupPositions(String s) {

        List<List<Integer>> list= new ArrayList<>();
        int i=0;
        int n=s.length();
        while(i<n-1){
            int j=i;
            while(j<n && (s.charAt(j)==s.charAt(i))){
               j++;
            }
            
            if(j-i>2){
                list.add(Arrays.asList(i, j-1));
            }

            i=j;
        }
        return list;

    }
}