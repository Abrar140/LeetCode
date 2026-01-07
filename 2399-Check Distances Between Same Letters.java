class Solution {
    public boolean checkDistances(String s, int[] distance) {
        int[] first= new int[26];
        Arrays.fill(first, -1);

        for(int i=0; i<s.length(); i++){

            int count= s.charAt(i)-'a';
            if(first[count]==-1){
                first[count]=i; 

            }else{
                first[count]=i- first[count]-1; 
                 if(distance[count] != first[count]){
                return false;
            }

            }
        }

      
        
return true;
        
    }
}