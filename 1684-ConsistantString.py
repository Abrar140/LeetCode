class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
   
        count=0
        for word in words:
            count=count+1
            for letter in word:
                if letter not in allowed:
                    count=count-1
                    break
        return count


allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(Solution().countConsistentStrings(allowed,words))