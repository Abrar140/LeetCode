class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result=""
        while columnNumber>0:
            print(columnNumber)
            columnNumber-=1
            result=chr((columnNumber)%26+65)+result
            columnNumber//=26
 
        return result

columnNumber=701
s=Solution()
print(s.convertToTitle(columnNumber))