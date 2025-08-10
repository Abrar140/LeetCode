class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        countpositive = 0
        countnegative = 0
        for num in nums:
            if num > 0:
                countpositive += 1
            elif num < 0:
                countnegative += 1
        return max(countpositive, countnegative)



nums = [-2,-1,-1,1,2,3]
print(Solution().maximumCount(nums))