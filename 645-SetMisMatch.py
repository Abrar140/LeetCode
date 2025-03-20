class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output={}
        for num in nums:
            output[num]=output.get(num,0)+1
        missing=0
        for i  in range(1,len(nums)+1):
            if i not in output:
                missing=i
        duplicate= max(output, key=output.get)
            
        return [duplicate, missing]
      
       


nums = [2,2]
solution = Solution()
print(solution.findErrorNums(nums))