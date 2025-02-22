class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output={}
        for i in range(len(nums)):
            if nums[i] not in output:
                output[nums[i]]=1
            else:
                output[nums[i]]+=1

        return [key for key, value in output.items() if value == 2]
        


nums = [0,1,1,0]
solution = Solution()
print(solution.getSneakyNumbers(nums))