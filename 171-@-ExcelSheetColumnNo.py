class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sum = 0
        for i in range(len(columnTitle)):
            sum = sum * 26 + alphabets.index(columnTitle[i]) + 1
        return sum
        


columnTitle = "ABC"
print(Solution().titleToNumber(columnTitle))