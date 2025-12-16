class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, columns=len(matrix), len(matrix[0])
        newmatrix=[[0]*rows  for _ in range(columns)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                newmatrix[j][i]= matrix[i][j]
                
        return newmatrix     