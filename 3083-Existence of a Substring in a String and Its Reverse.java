class Solution {
    public boolean isSubstringPresent(String s) {

        Set<String> set= new HashSet();

        for(int i=0; i<s.length()-1; i++){
            if(s.charAt(i)==s.charAt(i+1)){
                return true;
            }
            String sts=s.charAt(i)+ "" +s.charAt(i+1);
            if(set.contains(sts)){
                return true;
            }
            String st=s.charAt(i+1)+ "" +s.charAt(i);
            set.add(st);
        }
        
        return false;
    }
}