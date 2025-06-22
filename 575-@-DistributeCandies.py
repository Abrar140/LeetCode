class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        return min(len(set(candyType)),len(candyType)//2)
        



candyType = [1,1,2,2,3,3]
print(Solution().distributeCandies(candyType))