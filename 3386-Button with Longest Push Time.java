class Solution {
    public int buttonWithLongestTime(int[][] events) {

        int prev=events[0][1];
        int index=events[0][0];
        int max=prev;

        for(int i=1; i<events.length; i++){
            if(events[i][1]- events[i-1][1]> max){
                max=events[i][1]- events[i-1][1];
                index= events[i][0];
            }else if(events[i][1]- events[i-1][1]== max && index> events[i][0]){
                                index= events[i][0];


            }
         prev=events[i][1];

        }

        return index;
        
    }
}