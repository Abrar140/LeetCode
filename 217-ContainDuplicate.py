class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict={}
        for i in nums:
            if i in dict:
                return True
            else:
                dict[i]=1
        return False


nums = [1,2,3,1]
solution = Solution()
print(solution.containsDuplicate(nums))

# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         return len(nums) != len(set(nums))