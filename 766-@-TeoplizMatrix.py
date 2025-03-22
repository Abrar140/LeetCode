class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        daigonals=defaultdict(list)

       
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                daigonals[i-j].append(matrix[i][j])

            
        for i in daigonals.values():
            if len(set(i))>1:
                return False
        return True


matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
solution = Solution()    
print(solution.isToeplitzMatrix(matrix))