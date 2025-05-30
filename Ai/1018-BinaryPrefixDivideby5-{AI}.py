

class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        result = []
        num = 0  # Store the binary number as an integer
        
        for bit in nums:
            num = (num * 2 + bit) % 5  # Keep remainder to avoid large numbers
            print(num, bit,num*2,num*2+bit, num*2+bit%5)
            result.append(num == 0)  # True if divisible by 5
        
        return result

# Example Usage:
nums = [0, 1, 1, 1, 1, 1]
solution = Solution()
print(solution.prefixesDivBy5(nums))  # Output: [True, False, False, False, True, False]
