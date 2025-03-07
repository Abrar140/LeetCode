class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i , index in enumerate(nums):
            if sum(nums[:i])==sum(nums[i+1:]):
                return i  
        return -1

            # print(i , index, nums[:i], nums[i:], sum(nums[:i]), sum(nums[i:]))


nums = [2,3,-1,8,4]
solution = Solution()
print(solution.findMiddleIndex(nums))
