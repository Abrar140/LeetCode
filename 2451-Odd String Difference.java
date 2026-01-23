class Solution {
    public String oddString(String[] words) {
        int[][] str = new int[words.length][words[0].length() - 1];

        for (int i = 0; i < words.length; i++) {
            for (int j = 0; j < words[i].length() - 1; j++) {
                str[i][j] = words[i].charAt(j + 1) - words[i].charAt(j);
            }
        }
    int index=0;
    for(int j=0; j<str[0].length; j++){
  for(int i=0;i<str.length-2 ; i++ ){
    if(str[i][j]!= str[i+1][j] ||  str[i][j]!= str[i+2][j] || str[i+2][j]!= str[i+1][j] ){
        if(str[i][j]!= str[i+1][j] && str[i][j]== str[i+2][j]){
            index= i+1;
            break;
        } else  if(str[i][j]!= str[i+2][j] &&  str[i][j]== str[i+1][j]){
            index= i+2;
            break;
        } else{
            index=i;
            break;
        }
    }
  }
            
        }

   return words[index];
        

    }
}