# class Solution(object):
#     def maximumProduct(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         maximum1=0
#         maximum2=0
#         maximum3=0
#         for x  in nums:
#           if abs(x)>abs(maximum1):
#             maximum3=maximum2
#             maximum2=maximum1
#             maximum1=x
#           elif abs(x)>abs(maximum2):
#             maximum3=maximum2
#             maximum2=x
#           elif abs(x)>abs(maximum3):
#             maximum3=x
#         return maximum1*maximum2*maximum3



class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[0]*nums[1]* nums[-1], nums[-1]*nums[-2]*nums[-3])
    
          


nums =[-100,-98,-1,2,3,4]
instance = Solution()
print(instance.maximumProduct(nums))  