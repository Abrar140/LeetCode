class Solution {
    public boolean equalFrequency(String word) {
        int[] alpha= new int[26];
        int[] words=new int[100];
        List<Integer> list = new ArrayList<>();

        for(char w:word.toCharArray()){
            alpha[w-'a']++;
        }
        
   for(int l:alpha ){
    if(l!=0){
        words[l-1]++;

    }
        }


  



        for(int l:alpha ){
            if(l!=0 && !list.contains(l)){
                list.add(l);

            }
        }

             
        if(list.size()==1 && list.get(0)==1){
            return true;
        }
        if(list.size()!=2){
            return false;
        }
        if(size==2){
            
        }
        


       return Math.abs(list.get(0)-list.get(1))==1? true:false;
    }
}