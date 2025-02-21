class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        return int((s.count(letter)/float(len(s)))*100)
        

s = "foobar"
letter = "o"
instance = Solution()
print(instance.percentageLetter(s, letter))