class Solution {
    public int maxFreqSum(String s) {
        int[] alphabet= new int[26];
          for(char str: s.toCharArray()){
            alphabet[str-'a']++;
          }

        int vowelmax=0;
        int consonantmax=0;
        for (int i = 0; i < 26; i++) {
            char letter = (char) ('a' + i);

            if (letter == 'a' || letter == 'e' || letter == 'i'
                    || letter == 'o' || letter == 'u') {
                vowelmax = Math.max(vowelmax, alphabet[i]);
            } else {
                consonantmax = Math.max(consonantmax, alphabet[i]);
            }
        }
        
        return vowelmax + consonantmax;
        
        
    }
}