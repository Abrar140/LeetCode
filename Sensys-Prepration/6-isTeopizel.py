class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        for r in range(1, rows):
           
            for c in range(1, cols):
                print(r, rows, cols, c,  matrix[r][c], matrix[r-1][c-1])
                if matrix[r][c] != matrix[r-1][c-1]:
                    return False
        return True


matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
solution = Solution()    
print(solution.isToeplitzMatrix(matrix))
