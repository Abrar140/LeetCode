class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        buffs=[]
        bufft=[]
        for i in s:
            if i=="#":
                if len(buffs)>0:
                    buffs.pop()
            else:
                buffs.append(i)
        for i in t:
            if i=="#":
                if len(bufft)>0:
                    bufft.pop()
            else:
                bufft.append(i)
        
        return buffs==bufft



s = "abrar####"
t = "shafeeq"
instance = Solution()
print(instance.backspaceCompare(s,t))






# class Solution(object):
#     def backspaceCompare(self, s, t):
#         def finalString(string):
#             skip = 0
#             final = []
#             for char in reversed(string):
#                 if char == "#":
#                     skip += 1
#                 elif skip > 0:
#                     skip -= 1
#                 else:
#                     final.append(char)
#                     print(char)

#             return ''.join(final)

#         return finalString(s) == finalString(t)