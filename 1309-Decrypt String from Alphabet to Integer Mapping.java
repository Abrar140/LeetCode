class Solution {
    public String freqAlphabets(String s) {
        
        StringBuilder str= new StringBuilder();

        int j=s.length()-1;

        while(j>=0){
        if (s.charAt(j) == '#'){
                  int num= Integer.parseInt(s.substring(j-2, j));
                  System.out.println("this is my njum"+num+" ");
                   str.append ((char)(num-1+'a'));

                j=j-3;
            }else{
                str.append((char)(s.charAt(j)+'a'-'1'));
                j--;
            }

        }
        return str.reverse().toString();
    }
}