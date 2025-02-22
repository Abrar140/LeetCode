class Solution(object):
    def findDuplicates(self, nums):
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
        
        


nums = [4,3,2,7,8,2,3,1]
solution = Solution()
print(solution.findDuplicates(nums))