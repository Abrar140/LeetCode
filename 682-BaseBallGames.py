class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack=[]
        for i in operations:
            if i=="C":
                stack.pop()
            elif i=="D":
                stack.append(stack[-1]*2)
            elif i=="+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(i))
        return sum(stack)
         

ops = ["5","2","C","D","+"]

ans = Solution()
print(ans.calPoints(ops))