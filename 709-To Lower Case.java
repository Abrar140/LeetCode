class Solution {
    public String toLowerCase(String s) {
        StringBuilder output= new StringBuilder();
        for(char letter:s.toCharArray()){
            if(letter-'A'>=0 && letter-'A'<26){
                output.append((char)(letter+32));

            }else{
                output.append(letter);
            }
        }
        return output.toString();
    }
}