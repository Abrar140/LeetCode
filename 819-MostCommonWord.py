import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = re.findall(r'\b\w+\b', paragraph)
        output = {}
        for word in words:
            word=word.lower()
            if word not in banned:
                if word in output:
                    output[word] += 1
                else:
                    output[word] = 1
        

        return max(output,key=output.get)
      



paragraph = "Bob hit a ball, the hit BALL flew far after it was hit." 
banned = ["hit"]

print(Solution().mostCommonWord(paragraph, banned))