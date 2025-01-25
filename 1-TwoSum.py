class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result=[]
        for i in range(len(nums)):
            output=target-nums[i]
            if output in nums:
                index = nums.index(output)
                if i == index:
                    continue
                result.append(i)
                result.append(index)
                break

        return result
             


# Example usage
nums = [3,2,4]
instance = Solution()
print(instance.twoSum(nums, 6))  
