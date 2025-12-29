import java.util.*;

class Solution {
    public int minOperations(List<Integer> nums, int k) {
        int count = 0;
        List<Integer> arr = new ArrayList<>();

        for (int i = 1; i <= k; i++) {
            arr.add(i);
        }

        while (!arr.isEmpty() && !nums.isEmpty()) {
            int num = nums.remove(nums.size() - 1);

            if (arr.contains(num)) {
                arr.remove(Integer.valueOf(num));
            }

            count++;
        }

        return count;
    }
}
