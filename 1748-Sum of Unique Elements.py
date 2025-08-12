class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output={}
        unique_sum = 0
        for num in nums:
            if num  in output:
                output[num] += 1
            else:
                output[num] = 1

        for num, count in output.items():
            if count == 1:
                unique_sum += num


        return unique_sum
            
        


nums = [1, 2, 3, 2]
sol = Solution()
print(sol.sumOfUnique(nums))