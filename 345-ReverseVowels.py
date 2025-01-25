# class Solution(object):
#     def reverseVowels(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         s=list(s)   
#         endindex=len(s)-1
#         for x in range(len(s)):
#             if s[x]=='A'or s[x]=='a' or s[x]=='E'or s[x]=='e' or s[x]=='I'or s[x]=='i' or s[x]=='O'or s[x]=='o' or s[x]=='U'or s[x]=='u' :
#                 for y in range(endindex,0,-1):
#                     if x==y or y<x:
#                         return ''.join(s)
#                     else:
#                         if s[y]=='A'or s[y]=='a' or s[y]=='E'or s[y]=='e' or s[y]=='I'or s[y]=='i' or s[y]=='O'or s[y]=='o' or s[y]=='U'or s[y]=='u' :
#                          s[x], s[y]=s[y],s[x]
#                          endindex=y
#                          endindex=endindex-1
#                          break

#         return ''.join(s)



# # Example usage
# s = "IceCreAm"
# instance = Solution()
# print(instance.reverseVowels(s))  






def reverseVowels(s: str) -> str:
    # Define vowels
    vowels = set("aeiouAEIOU")
    
    # Convert string to list for mutability
    s_list = list(s)
    
    # Initialize two pointers
    left, right = 0, len(s_list) - 1
    
    while left < right:
        # Move the left pointer to the next vowel
        while left < right and s_list[left] not in vowels:
            left += 1
        
        # Move the right pointer to the previous vowel
        while left < right and s_list[right] not in vowels:
            right -= 1
        
        # Swap the vowels
        if left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
    
    # Join the list back into a string
    return ''.join(s_list)

# Example usage
s = "IceCreAm"
output = reverseVowels(s)
print(output)  # Output: "AceCreIm"
