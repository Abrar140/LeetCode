class Solution {
    public boolean buddyStrings(String s, String goal) {
        int s1= s.length();
        int g1=goal.length();
        if(s1!=g1 || s1==1){
            return false;
        }


        int count=0;
        int value=0;
        char[] str= new char[2];
        char[] gl= new char[2]; 
        for(int i=0; i<s1; i++){
          if(s.charAt(i)!= goal.charAt(i)){
            if (value==2){
                return false;
            }
             str[value]=s.charAt(i);
             gl[value]= goal.charAt(i);
             value++;
            count++;
          }
        }
        
        if(count>2 || count ==1) return false;

        if((str[0]==gl[1]&& str[1]==gl[0]) && count==2){
            return true;
        }
        if(count==0){
           

           int[] alpha= new int[26];
            for(char c: s.toCharArray()){
             alpha[c-'a']++;
            }
           int cnt=0;
           for(int a: alpha){
            if (a!=0){
                cnt++;
                if(a>=2){
                return true;
            }
            }
            
           }

           if(cnt==1){
            return true;
           }
           

        }
    

        return false;

        
    }
}