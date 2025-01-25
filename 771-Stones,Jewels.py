class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count=0
        for x in stones:
            for y in jewels:
                if x==y:
                    count=count+1
        return count



# Example usage
jewels = "BB"
stones = "aAAbbbb"
instance = Solution()
print(instance.numJewelsInStones(jewels, stones))  