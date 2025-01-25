class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        outputrray=[]
        for i in range(n):
            outputrray.append(nums[i])
            outputrray.append(nums[i+n])
        return outputrray
             


# Example usage
nums = [2,5,1,3,4,7]
instance = Solution()
print(instance.shuffle(nums, 3))  
