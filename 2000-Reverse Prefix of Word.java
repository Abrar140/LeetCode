class Solution {
    public String reversePrefix(String word, char ch) {

        int left=0;
        int right=0;
        for(int i=0;i<word.length(); i++){

            if(ch==word.charAt(i)){
                right=i;
                break;
            }
        }

        if(right==0){
            return word;
        }
        char[] arr= word.toCharArray();
        
        while(left<right){
           char temp=arr[left];
            arr[left]=arr[right];
            arr[right]= temp;
            left++;
            right--;
        
        }

        return new String(arr);
        
    }
}