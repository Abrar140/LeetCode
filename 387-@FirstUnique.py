# class Solution(object):
#     def firstUniqChar(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         output={}
#         for i in s:
#             if i not in output:
#                 output[i]=1
#             else:
#                 output[i]+=1
#         uniquevalue=None
#         for key, value in output.items():
#             if value == 1:
#                 uniquevalue=key
#                 break

#         for i in range(len(s)):
#             if(s[i]==uniquevalue):
#                 return i
        
#         return -1

        
class Solution(object):
    def firstUniqChar(self, s):
        count={}
        for char in s:
            count[char]=count.get(char,0)+1

        for index, char in enumerate(s):
            if count[char]==1:
                return index
        return -1
      

















s = "loveleetcode"
sol=Solution()
print(sol.firstUniqChar(s))
