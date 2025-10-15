class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        firstrow="qwertyuiop"
        secondrow="asdfghjkl"
        thirdrow="zxcvbnm"
        output=[]
        needed=True
        for word in words:
            word2=word.lower()
            if(word2[0] in firstrow):
                for letter in word2:
                    if letter not in firstrow:
                        needed=False
                if needed==False:
                    needed=True
                else:
                    output.append(word)

            elif(word2[0] in secondrow):
                for letter in word2:
                    if letter not in secondrow:
                        needed=False
                if needed==False:
                    needed=True
                else:
                    output.append(word)

            elif(word2[0] in thirdrow):
                for letter in word2:
                    if letter not in thirdrow:
                        needed=False
                if needed==False:
                    needed=True
                else:
                    output.append(word)


        return output




        