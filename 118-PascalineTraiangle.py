class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output=[]
        for i in range(numRows):
            output.append([1]*(i+1))

        for i in range(2, numRows):
            for j in range(1, i):
                output[i][j]=output[i-1][j-1]+output[i-1][j]
        return output

        

numRows = 5
print(Solution().generate(numRows))