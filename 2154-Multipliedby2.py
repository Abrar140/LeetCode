class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        while original in nums:
            original *= 2
        return original
    


nums = [5,3,6,1,12]
original = 3

solution = Solution()
print(solution.findFinalValue(nums, original))