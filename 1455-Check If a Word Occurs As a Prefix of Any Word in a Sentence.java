class Solution {
    public int isPrefixOfWord(String sentence, String searchWord) {

        int output=-1;
        String[] arr= sentence.trim().split("\\s+");
        for(int i=0; i<arr.length; i++){
            if(arr[i].startsWith(searchWord)){
                output=i+1;
                break;
            }
        }

        return output;
        
    }
}