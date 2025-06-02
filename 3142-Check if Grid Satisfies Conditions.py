class Solution(object):
    def satisfiesConditions(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        numberofrows=len(grid)
        noofcolumns=len(grid[0])
        for i in range(numberofrows):
            for j in range(noofcolumns):
                if j+1<noofcolumns:
                    if grid[i][j]==grid[i][j+1]:
                     return False
                if i+1<numberofrows:
                    if grid[i][j]!=grid[i+1][j]:
                     return False
     
        return True
               
     



        


grid = grid =[[1],[2],[3]]
solution = Solution()
print(solution.satisfiesConditions(grid))