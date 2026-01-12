class Solution {
    public void reverse(StringBuilder sb){
      sb.reverse();

    }
    public String finalString(String s) {
        StringBuilder sb= new StringBuilder();
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i)=='i'){
                reverse(sb);
            }else{
                sb.append(s.charAt(i));
            }
        }
           return sb.toString();
    }
}