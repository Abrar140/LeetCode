class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        acronym = ""
        for word in words:
            acronym += word[0]
        return acronym == s







words = ["alice","bob","charlie"]
s = "abc"
print(Solution().isAcronym(words, s))