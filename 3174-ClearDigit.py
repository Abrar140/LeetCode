class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        output=[]
        for i in s:
            if i in "0123456789":
                output.pop()
            else:
                output.append(i)
        return ''.join(output)


s = "abc"
sol= Solution()
print(sol.clearDigits(s))