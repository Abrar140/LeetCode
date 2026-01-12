import java.util.*;

class Solution {
    public boolean isPathCrossing(String path) {
        int x=0;
        int y=0;

        Set<String> set= new HashSet<>();
         String st= x+","+y;
         set.add(st);


        for(char c: path.toCharArray()){
            if(c=='N'){
             y++;

            } else   if(c=='E'){
                x++;

            }  else   if(c=='S'){
                y--;

            }else{
                x--;

            }
            String str=  x+","+y;
            if(set.contains(str)){
                return true;
            }else{
                set.add(str);
            }
        }
        


        return false;
        
    }
}










