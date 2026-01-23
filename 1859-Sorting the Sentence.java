class Solution {
    public String sortSentence(String s) {
        String[] str= s.split("\\s+");
        String[] sort= new String[str.length];

        for(String st:str){
            int length=st.length()-1;
            sort[st.charAt(length)- '1']=st.substring(0,length );
        }

        StringBuilder strng= new StringBuilder();
        for(String st:sort){
            strng.append(st);
            strng.append(" ");
        }


        return strng.toString().trim();
    }
}