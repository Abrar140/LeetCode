class Solution {
    public int maxDepth(String s) {
        int leftbracket=0;
        int rightbracket=0;
        int maxdepth=0;
        for(char c:s.toCharArray() ){
            if(c=='('){
                leftbracket++;
            }else if(c==')'){
                rightbracket++;
            }
               
             maxdepth=Math.max(maxdepth,  leftbracket - rightbracket );
 

        }

        return maxdepth;
        
    }
}