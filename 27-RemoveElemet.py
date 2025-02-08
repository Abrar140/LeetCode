class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        current=0
        while current<len(nums):
            if nums[current]==val:
                nums.pop(current)
            else:
                current=current+1
        print(nums)
        return (len(nums))



nums = [3,2,2,3]
val = 3
instance=Solution()
print(instance.removeElement(nums, val))