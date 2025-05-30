# class Solution(object):
#     def lengthOfLastWord(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """

#         return len(s.split()[-1])



class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        i = len(s) - 1
        print(i)

        while i >= 0 and s[i] == ' ':
    
            i -= 1



        while i >= 0 and s[i] != ' ':
           
            length += 1
            i -= 1

        return length

s = "   fly me   to   the moon  "

print(Solution().lengthOfLastWord(s))