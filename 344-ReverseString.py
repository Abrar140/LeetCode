class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for x in range(len(s)//2):
            s[x],s[len(s)-x-1]=  s[len(s)-x-1], s[x]
        return s


# class Solution(object):
#     def reverseString(self, s):
#         """
#         :type s: List[str]
#         :rtype: None Do not return anything, modify s in-place instead.
#         """
#         outputarray=[]
#         for i in range(len(s), 0, -1):
#             outputarray.append(s[i-1])
        
#         return outputarray





# Example usage
s = ["H","a","n","n","a","h"]
instance = Solution()
print(instance.reverseString(s))  