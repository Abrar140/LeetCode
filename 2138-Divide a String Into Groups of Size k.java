class Solution {
    public String[] divideString(String s, int k, char fill) {
        
        int n=s.length();
        int length;
        if(n%k==0){
            length=n/k;
        }else{
          length=(n/k)+1;
        }
        String[] r= new String[length];
        length=0;

        StringBuilder str= new StringBuilder();

        for(int i=0; i<n; i++){

            if(i!=0 && i%k==0){
                r[length++]=str.toString();
                str.setLength(0);
            }

            str.append(s.charAt(i));

            
        }
        n=str.length();
        if(n==k){
            r[length++]=str.toString();

        }else{
            str.repeat(fill, k-n);
                r[length++]=str.toString();

        }

        return r;
    }
}