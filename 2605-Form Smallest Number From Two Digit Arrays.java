class Solution {
    public int minNumber(int[] nums1, int[] nums2) {

        int min1=Integer.MAX_VALUE;
        int min2=Integer.MAX_VALUE;

        for(int n: nums1){
            if(min1>n){
                min1=n;
            }
        }

         for(int n: nums2){
            if(min2>n){
                min2=n;
            }
        }

        Set<Integer> set = new HashSet<>();
        for(int n: nums1){
                set.add(n);
            
        }
    
    int ret=10;
     
  
for(int n: nums2){
    if(set.contains(n) && n<ret){
        ret=n;
    }
            
        }

if(ret!=10){
    return ret;
}

if(min1>min2){
            return  min2*10+min1;
 
}



        return  min1*10+min2;


        
    }
}