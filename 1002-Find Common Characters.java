class Solution {
    public List<String> commonChars(String[] words) {
        

        List<String> first= new ArrayList<>();
        for(char c: words[0].toCharArray()){
           first.add(String.valueOf(c));
        }
        
        for (int i=1; i<words.length; i++){
            List<String> ne = new ArrayList<>(first);

             for(char c: words[i].toCharArray()){
                if (first.contains(String.valueOf(c))) {
                  ne.remove(String.valueOf(c));

                }
            }

            while(!ne.isEmpty()){
               String p = ne.remove(0);
                first.remove(p);
            }


        }

        return first;
    }
}