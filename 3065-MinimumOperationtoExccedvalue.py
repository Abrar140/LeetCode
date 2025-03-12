class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return nums.min()
        

nums = [2,11,10,1,3]
k = 10
sol=Solution()
print(sol.minOperations(nums,k))