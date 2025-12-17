import java.util.*;

class Solution {
    public int countGoodSubstrings(String s) {
        List<String> returnedSet = new ArrayList<>();
        for(int i=0; i<s.length()-2; i++){
            StringBuilder sized=new   StringBuilder();
            sized.append(s.charAt(i)).append(s.charAt(i+1)).append(s.charAt(i+2));
            if(s.charAt(i)!=s.charAt(i+1) && s.charAt(i)!=s.charAt(i+2) && s.charAt(i+1)!=s.charAt(i+2)){
             returnedSet.add(sized.toString());
            }
        }

        return returnedSet.size();

    }
}  