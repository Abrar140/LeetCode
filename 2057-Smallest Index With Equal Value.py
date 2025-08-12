class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
        return -1

nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
sol = Solution()
print(sol.smallestEqual(nums))