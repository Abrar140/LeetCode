class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int] 
        """
        output=[]
        for i in range(rowIndex+1):
            output.append([1]*(i+1))

        for i in range(2, rowIndex+1):
            for j in range(1,i):
                output[i][j]=output[i-1][j-1]+output[i-1][j]

        return output[rowIndex]

        

rowIndex=3
print(Solution().getRow(rowIndex))