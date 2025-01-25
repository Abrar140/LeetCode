class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum =[]
        for index, x in enumerate(nums):
          print(x, index)
          running_sum.append(sum(nums[:index+1]))
          
        return running_sum
           
nums=[1,2,3,4]   
instance=Solution()
print(instance.runningSum(nums))          