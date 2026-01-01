class Solution {
    public String decodeMessage(String key, String message) {
        Map<Character, Character> map= new HashMap<>();
        char c='a';
        for(char k:key.toCharArray() ){
            if(!map.containsKey(k) && k != ' '){
                map.put(k, c);
                c++;
            }
        }
        StringBuilder str= new StringBuilder();
        for(char m: message.toCharArray()){
            if(m==' '){
                str.append( ' ');
            }else{
                str.append(map.get(m));
            }
        }

        return str.toString();
        
    }
}