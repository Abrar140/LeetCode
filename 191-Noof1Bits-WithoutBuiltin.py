class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n:
            if n & 1:         # Check if last bit is 1
                count += 1
                print(count,"......",n)
            n = n >> 1        # Shift right by 1 (remove last bit)
            print(n)
        return count



n=11
instance = Solution()
print(instance.hammingWeight(n))