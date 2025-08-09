class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        count=0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + diff == nums[j]:
                    for k in range(j+1, len(nums)):
                        if nums[j] + diff == nums[k]:
                            count += 1
        return count



nums = [0,1,4,6,7,10]
diff = 3
print(Solution().arithmeticTriplets(nums, diff))