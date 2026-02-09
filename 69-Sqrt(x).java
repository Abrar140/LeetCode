class Solution {
    public int mySqrt(int x) {
        if (x == 0 || x == 1) return x;

        int i = 1;
        for (; (long)i * i <= x; i++) {
            if ((long)i * i == x) {
                return i;
            }
        }
        return i - 1;
    }
}
