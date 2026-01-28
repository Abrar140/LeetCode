class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> list= new ArrayList<>();

        int top = 0, left = 0;
        int bottom = matrix.length - 1;
        int right = matrix[0].length - 1;

        int dir=0;
        int j=0, k=0;
        for(int i=0; i<(matrix.length* matrix[0].length); i++){
            list.add(matrix[k][j]);
            if(dir==0){
                if(j<right) j++;
                else{
                    dir=1;
                    top++;
                    k++;
                }

            }else if(dir==1){

                 if(k<bottom) k++;
                else{
                    dir=2;
                    right--;
                    j--;
                }

            } else if (dir == 2) {        
    if (j > left) j--;
    else {
        dir = 3;
        bottom--;
        k--;
    }

} else {                     
    if (k > top) k--;
    else {
        dir = 0;
        left++;
        j++;
    }
}

        }

return list;
        
    }
}