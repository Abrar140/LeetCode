class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [sum(nums[x] > nums[y] for y in range(x+1, len(nums))) for x in range(len(nums))]


nums = [5,2,6,1]

print(Solution().countSmaller(nums))