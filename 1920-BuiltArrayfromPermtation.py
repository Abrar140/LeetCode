class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[]
        for i in range(len(nums)):
            output.append(nums[nums[i]])

        return output        



nums = [0,2,1,5,3,4]
solution = Solution()
print(solution.buildArray(nums))













