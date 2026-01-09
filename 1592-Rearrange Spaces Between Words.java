class Solution {
    public String reorderSpaces(String text) {
        
        int spaces=0;
        String[] words= text.trim().split("\\s+");
        for(int t=0; t< text.length(); t++){
            int i= text.charAt(t);
            if(i==' '){
                spaces++;
            }
        
        }
        int n= words.length;
        StringBuilder str= new StringBuilder();

        if(n==1){
         str.append(words[0]);
         str.append(" ".repeat(spaces));
         
        return  str.toString();

        }
        int eqspaces= spaces/(n-1);
        for(int i=0; i<words.length; i++){
           str.append(words[i]);
           if(i!= n-1){
              str.append(" ".repeat(eqspaces));
           }

        }
        

          str.append(" ".repeat(spaces-(eqspaces * (n-1))));



      


        return  str.toString();
    }
}