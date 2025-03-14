class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        """
        :type n: int
        :type commands: List[str]
        :rtype: int
        """
        row=0
        column=0
        for  command in commands:
            if command == "RIGHT":
                column+=1
            elif command == "LEFT":
                column-=1
            elif command == "DOWN":
                row+=1
            elif command == "UP":
                row-=1
        
        return (row*n)+column




n = 3
commands = ["DOWN","RIGHT","UP"]

solution = Solution()
print(solution.finalPositionOfSnake(n, commands))