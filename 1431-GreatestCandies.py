class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        return [True if candies[i]+extraCandies>=max(candies) else False for i in range(len(candies))]
        


candies = [2,3,5,1,3]
extraCandies = 3

print(Solution().kidsWithCandies(candies, extraCandies))