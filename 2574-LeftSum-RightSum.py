class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[]
        for i  in range(len(nums)):
            value= abs(sum(nums[i+1:])- sum(nums[:i]))
            output.append(value)
        return output        
nums = [10,4,8,3]
solution = Solution()
print(solution.leftRightDifference(nums))