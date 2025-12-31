class Solution {
    public int findKthPositive(int[] arr, int k) {
        int [] array= new int[k];
        int number=0;
        Set<Integer> set= new HashSet<>();
        for(int n: arr){
            set.add(n);
        }
        int numb=1;
        while(number<k){

            if(!set.contains(numb) ){
                array[number]=numb;
                number++;
                numb++;
            }else{
                numb++;
            }
        }

        return array[k-1];
    }
}