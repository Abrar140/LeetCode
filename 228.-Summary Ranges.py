class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        start = 0
        end = len(nums) - 1
        result = []
        
        for i in range(len(nums)):
            if start == end:
                result.append(str(nums[start]))
                break
            if i + 1 < len(nums) and nums[i + 1] - nums[i] == 1:
                continue
            else:
                end = i
                if start == end:
                    result.append(str(nums[start]))
                else:
                 result.append(str(nums[start]) + "->" + str(nums[end]))
                 
                start = i + 1
                end = len(nums) - 1
                
        return result


nums = [0,2,3,4,6,8,9]
print(Solution().summaryRanges(nums))