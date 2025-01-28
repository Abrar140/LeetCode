class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0, len(nums)+1):
            if i not in nums:
                return i
            
       

nums=[3,4,1,2]
solution = Solution()
print(solution.missingNumber(nums))




# class Solution(object):
#     def missingNumber(self, nums):
#         n=len(nums)
#         m=n*(n+1)//2
#         print(n,m,sum(nums))
#         return m-sum(nums)