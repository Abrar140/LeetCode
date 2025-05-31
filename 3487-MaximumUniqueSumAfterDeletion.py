class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output={}
        sum=0
        for i in range(len(nums)):
            if nums[i] not in output:
                output[nums[i]]=1
            else:
                output[nums[i]]+=1
        
        print(output)

        for index, value in output.items():
            if index>0:
                sum+=index

        if sum==0:
            return  max(nums)

        return sum
       
        


nums = [1,2,-1,-2,1,0,-1]
solution = Solution()
print(solution.maxSum(nums))