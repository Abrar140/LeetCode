class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result=s.split(":")
        start=result[0][1]
        end=int(result[1][1])
        print(result[0][1],result[1][1])
        for i in range(start,end+1):
            print(i)
        return result


s = "K1:L2"
obj = Solution()
print(obj.cellsInRange(s))