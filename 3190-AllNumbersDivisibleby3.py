class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operation=0
        for i in nums:
            if i%3!=0:
                operation+=1

        return operation



nums = [1,2,3,4,5,6]
solution = Solution()
print(solution.minimumOperations(nums))