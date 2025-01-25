class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        reult=""
        for x in range(1, columnNumber+1):
            reult=chr((columnNumber-1)%26+65)+reult
            columnNumber=(columnNumber-1)//26
        return reult

columnNumber=40
s=Solution()
print(s.convertToTitle(columnNumber))