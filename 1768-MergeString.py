class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        lengthofoutput=len(word1)+len(word2)
        outputstring=""
        for  x  in range(lengthofoutput):
          if x<len(word1):
            outputstring=outputstring + word1[x]
          if x<len(word2):
            outputstring=outputstring + word2[x]
        return outputstring



word1 = "ab"
word2 = "pqrnmbre"


instance = Solution()
print(instance.mergeAlternately(word1, word2))    