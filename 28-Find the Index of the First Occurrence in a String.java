class Solution {
    public int strStr(String haystack, String needle) {
         int start = 0;
        int matchStart = 0;
        for(int i=0; i<haystack.length() ;i++){
            
            if(haystack.charAt(i)== needle.charAt(start)){

                 if (start == 0) {
                    matchStart = i; 
                }
                start++;
                if(start==needle.length() ){
                    return matchStart;
                }
            }else{
                   
                    System.out.println("the mismatch happens"+ i +" "+ start);
                    if(start>0){
                    i = matchStart;

                    }
                    start=0;
                    
               
            }


        }



        return -1;
        
    }
}