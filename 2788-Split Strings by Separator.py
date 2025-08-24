class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        result=[]
        for word in words:
            start=0
            for part in range(len(word)):
                if word[start] == separator:
                    start += 1
                    continue
                elif(part == len(word) - 1 and word[start] == separator):
                    continue
                elif word[part] == separator:
                    result.append(word[start:part])
                    start = part + 1
                elif part == len(word) - 1:
                    result.append(word[start:part + 1])



        return result

    




words = ["$easy$","$problem$"]
separator = "$"
obj = Solution()
print(obj.splitWordsBySeparator(words, separator))

