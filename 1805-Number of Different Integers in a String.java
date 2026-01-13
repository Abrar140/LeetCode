class Solution {
    public int numDifferentIntegers(String word) {
        Set<String> set= new HashSet<>();
        int index=0;

        for(int i=0; i<word.length(); i++){
             if(!Character.isDigit(word.charAt(i))){
              if(i>index){
                String st=word.substring(index,i);
                      st=st.replaceFirst("^0+", "");
                      if(st.isEmpty()){
                        st="0";
                      }
                      set.add(st);
              }
                 index=i+1;

            }
        }
          if (index < word.length()) {
            String st = word.substring(index);
            st = st.replaceFirst("^0+", "");
            if (st.isEmpty()) st = "0";
            set.add(st);
        }


        for(String s:set){
            System.out.println(s);
        }


        return set.size();
        
    }
}