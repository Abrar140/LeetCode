# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         for index, x  in enumerate(nums):
#             print("value is",index,x)
#             if  x==0:
#                 element=nums.pop(index)
#                 nums.append(element)
              
#         for index, x  in enumerate(nums):
#             print("value is",index,x)
#             if  x==0:
#                 element=nums.pop(index)
#                 nums.append(element)
        
#         return nums
#         # index = 0
#         # while index < len(nums):
#         #    x = nums[index]
#         #    print("value is", index, x)
#         #    if x == 0:
#         #       element = nums.pop(index)  # Remove the element at the current index
#         #       nums.append(element)       # Append it to the end
#         #       print("Moved 0 to the end. Updated list:", nums)
              
              
#         #    else:
#         #        index += 1  # Only move to the next index if no element was removed
            
class Solution(object):
    def moveZeroes(self, nums):
        nonzeroindex = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nonzeroindex],nums[i]=nums[i],nums[nonzeroindex]
                nonzeroindex += 1
             


# Example usage
nums = [0, 0, 0, 0, 0, 0, 1, 1, 1]
instance = Solution()
instance.moveZeroes(nums)  # The list is modified in place
print(nums)  # Print the modified list
