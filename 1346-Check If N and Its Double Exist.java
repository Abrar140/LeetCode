import java.util.*;
class Solution {
    public boolean checkIfExist(int[] arr) {
        List<Integer> list= new ArrayList<>();
        for(int a:arr){
            list.add(a);
        }

        for(int i=0; i<list.size(); i++){
            int a=list.get(i);
            int aby2=a*2;
            
            if( list.contains(aby2 ) ){
                int j= list.indexOf(aby2);

                if(i!=j){
                    return true;
                }
                


                }
            }

        

        

       

        return false;
        
    }
}
