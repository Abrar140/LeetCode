class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if sentence[0] != sentence[-1]:
            return False
        for i in range(1, len(sentence)):
            if sentence[i] == ' ' and sentence[i - 1] != sentence[i + 1]:
                return False
        return True


sentence = "leetcode exercises sound delightful"
solution = Solution()
print(solution.isCircularSentence(sentence))