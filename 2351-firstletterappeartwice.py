class Solution(object):
    def repeatedCharacter(self, s):
        count={}
        for char in s:
            if char in count:
                return char
            else:
                count[char]=1
          
        return -1



s = "abccbaacz"
instance = Solution() 
print(instance.repeatedCharacter(s)) 