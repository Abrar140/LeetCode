class Solution {
    public String greatestLetter(String s) {

        char letter= '\0';
        Set<Character>  set= new HashSet<>();
        for(char l:s.toCharArray()){
            set.add(l);
        }
         for(char l:s.toCharArray()){
            if (set.contains(Character.toLowerCase(l)) && set.contains(Character.toUpperCase(l))) {
                if(letter<l){
                    letter=l;
                }
            }
        }
       
       if (letter == '\0') {
            return "";
        }
        letter = Character.toUpperCase(letter);
        
        return Character.toString(letter);
    }
}