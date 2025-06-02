class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        dictforchars={}
        dictforwords={}
        for char in chars:
            if char in dictforchars:
                dictforchars[char]=dictforchars[char]+1
            else:
                dictforchars[char]=1
        found=""
        flag=False

        
        for word in words:
            if len(word)>len(chars):
                continue
            for letter in word:
                if letter in dictforwords:
                    dictforwords[letter]=dictforwords[letter]+1
                else:
                    dictforwords[letter]=1

            for letter in word:
                if letter in dictforchars:
                    if dictforwords[letter]>dictforchars[letter]:
                        flag=True
                        break
                else:
                    flag=True
                    break
               
            if flag:
                flag=False
            else:
                found=found+word

        
            print(dictforwords, dictforchars, found)
            dictforwords={}

        return len(found)



        #         if letter not in chars:
        #             flag=True
        #             break

        #     if flag:
        #         flag=False
        #     else:
        #          found=found+word

        # return len(found)

        
                


           
        

words=["caaat","bt","hat","tree"]
chars="atach"
sol = Solution()
print(sol.countCharacters(words, chars))