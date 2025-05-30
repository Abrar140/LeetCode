class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    nums.pop(j)
                else:
                    j += 1
            i += 1
        return nums

nums = [1, 2, 2, 3, 4, 3, 4, 3, 2, 2, 2, 1, 10]
solution = Solution()
print(solution.removeDuplicates(nums))
