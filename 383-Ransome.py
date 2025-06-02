class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dictformagzine = {}
        for i in magazine:
            if i in  dictformagzine:
                 dictformagzine[i] += 1
            else:
                 dictformagzine[i] = 1
        for i in ransomNote:
            if i in  dictformagzine:
                 dictformagzine[i] -= 1
                 if dictformagzine[i] < 0:
                     return False
            else:
                 return False
        return True
ransomNote = "a"
magazine = "b"