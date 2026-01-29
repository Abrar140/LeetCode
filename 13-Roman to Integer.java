class Solution {
    public int romanToInt(String s) {
Map<Character, Integer> roman = Map.of(
    'I', 1,
    'V', 5,
    'X', 10,
    'L', 50,
    'C', 100,
    'D', 500,
    'M', 1000
);

int i=s.length()-1;
int Sum=0;

while(i>0){
    int sec= roman.get(s.charAt(i-1));
    int lst=roman.get(s.charAt(i));
    if(sec<lst){
        Sum= Sum+(lst-sec);
        i=i-2;

    }else{
        Sum=Sum+lst;
        i--;
    }
}
if(i==0){
    Sum=Sum+roman.get(s.charAt(i));
}
 return Sum;
        
    }
}