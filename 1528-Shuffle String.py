class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        # return "".join(s[i] for i in indices)
        restored = [''] * len(s)
        for i, index in enumerate(indices):
            restored[index] = s[i]
        return ''.join(restored)


s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
sol=Solution()
print(sol.restoreString(s,indices))