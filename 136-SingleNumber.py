from functools import reduce

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return(reduce(lambda x, y: x ^ y, nums))
        # linear time O(n) and constant space O(1).
        

nums = [2,2,1]
solution = Solution()
print(solution.singleNumber(nums))