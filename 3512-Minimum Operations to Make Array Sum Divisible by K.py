class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        
        return sum(nums)%k


nums = [3,9,7]
k = 5
sol=Solution()
print(sol.minOperations(nums,k))