class Solution {
    public int canBeTypedWords(String text, String brokenLetters) {

     int noofletters= 0;
     boolean letters=false;
     
     
    for(char c: text.toCharArray()){
        if(c==' '){
            if(!letters){
            noofletters++;
            }
            letters=false;
        }else if(brokenLetters.indexOf(c)!=-1){
           letters=true;

        }
     }
     if(!letters){
                    noofletters++;

     }

     return noofletters;

        
    }
}