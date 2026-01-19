class Solution {
    public String interpret(String command) {
      StringBuilder str = new StringBuilder();

        boolean flag= false;
        for(char c: command.toCharArray()){
            if(c=='('){
                flag=true;
            }else if(c==')'){
                if(flag){
                str.append('o');
                }
                flag=false;
            }else if(flag || c !='(' && c!=')'){
              flag=false;
              str.append(c);
            }
        }

        return str.toString();
        
    }
}