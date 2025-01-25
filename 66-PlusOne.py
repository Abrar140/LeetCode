class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        String=""
        for x in digits:
            String=String+str(x)
        String=int(String)+1
        return [int(x) for x in str(String)]



digits = [1,2,3,9]

s = Solution()

print(s.plusOne(digits))