class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        else:
            index = word.index(ch)
            index=index+1
            for i in range(index//2):
                word[i], word[index-i-1]=word[index-i-1], word[i]
                print(word)

            
                print(i)
            print(index)
            return word[:word.index(ch)+1][::-1] + word[word.index(ch)+1:]
        


word = "abcdefd" 
ch = "d"


obj = Solution()
print(obj.reversePrefix(word, ch))