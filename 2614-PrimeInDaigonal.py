class Solution(object):

    def isPrime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    def diagonalPrime(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        maximum=0
        for i in range(len(nums)):
            if self.isPrime(nums[i][i]):
                    maximum=max(maximum,nums[i][i])
            if self.isPrime(nums[i][len(nums)-i-1]):
                    maximum=max(maximum,nums[i][len(nums)-i-1])
        return maximum
            # print(nums[i][i])
            # #  nums[i][i] = val or an i for which nums[i][nums.length - i - 1] = val.
        

nums = [[1,2,3],[5,6,7],[9,10,11]]
print(Solution().diagonalPrime(nums))
