class Solution {
    public int[] separateDigits(int[] nums) {
        StringBuilder str = new StringBuilder();

        for (int n : nums) {
            str.append(n);
        }
        int[] output= new int [str.length()];

        System.out.println(str);
        for(int i=0 ; i<str.length(); i++){
            output[i]= str.charAt(i)- '0';
            
        }


        return output;
    }
}
