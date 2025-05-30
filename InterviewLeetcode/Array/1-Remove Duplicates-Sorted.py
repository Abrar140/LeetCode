class Solution(object):
    def removeDuplicates(self, nums):
        current=0
        while current<len(nums)-1:
            if nums[current]==nums[current+1]:
                nums.pop(current+1)
            else:
                current=current+1
        return nums



nums=[1,1,2,3,4,4]
solution=Solution()
print(solution.removeDuplicates(nums))