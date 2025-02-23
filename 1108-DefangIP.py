# class Solution(object):
#     def defangIPaddr(self, address):
#         """
#         :type address: str
#         :rtype: str
#         """
        

#         return address.replace(".","[.]")


class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        result=''

        for ch in address:
            if ch == '.':
                result+= '[.]'
            else:
                result += ch
            
        return result

       

















address = "1.1.1.1"
print(Solution().defangIPaddr(address))