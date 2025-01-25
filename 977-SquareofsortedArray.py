class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output_array = [x * x for x in nums]
        output_array.sort()
        return  output_array

nums=[-4,-1,0,3,10] 
instance=Solution()
print(instance. sortedSquares(nums))   


     # for  x in nums:
        #     output_array.append(x*x)