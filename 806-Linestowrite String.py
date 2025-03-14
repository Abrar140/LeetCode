class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        alphabet_widths = {chr(97 + i): widths[i] for i in range(26)}
        lines=1
        width=0
        for i in s:
            width+=alphabet_widths[i]
            if width>100:
                lines+=1
                width=alphabet_widths[i]    
        return [lines,width]







#    def numberOfLines(self, widths, s):
#         lines = 1
#         width = 0
        
#         for char in s:
#             char_width = widths[ord(char) - ord('a')]  # Direct lookup
#             if width + char_width > 100:
#                 lines += 1
#                 width = char_width  # Reset width to the new character
#             else:
#                 width += char_width
        
#         return [lines, width]








widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s="abcdefghijklmnopqrstuvwxyz"

obj = Solution()
print(obj.numberOfLines(widths, s))