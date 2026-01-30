class Solution {
    public String reverseOnlyLetters(String s) {
        int left = 0;
        int right = s.length() - 1;
        char[] array = new char[right + 1];

        while (left < right) {
            if (Character.isLetter(s.charAt(left)) && Character.isLetter(s.charAt(right))) {
                array[left] = s.charAt(right);
                array[right] = s.charAt(left);

                left++;
                right--;
            } else if (Character.isLetter(s.charAt(left))) {
                array[right] = s.charAt(right);
                right--;
            } else if (Character.isLetter(s.charAt(right))) {
                array[left] = s.charAt(left);
                left++;
            } else {
                array[left] = s.charAt(left);
                array[right] = s.charAt(right);
                left++;
                right--;
            }
        }
        if(left==right){
                            array[left] = s.charAt(left);

        }

        return new String(array);
    }
}
