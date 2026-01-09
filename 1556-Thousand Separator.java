class Solution {
    public String thousandSeparator(int n) {

       StringBuilder str= new StringBuilder();
       int index=0;
       if(n==0){
        return "0";
       }
       
       while(n>0){
        str.append(n%10);
        n=n/10;
        index++;

         if(index%3==0 && n>0){
           str.append(".");
                }
       }
      

        return str.reverse().toString();
        
    }
}