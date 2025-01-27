# class Stack:
#     def __init__(self, size):
#         self.stack=[None]*size
#         self.top=-1
#         self.size=size
    
#     def push(self, value):
#         if self.top==self.size-1:
#             print ("Stack is full")
#         else:
#             self.top+=1
#             self.stack[self.top]=value

#     def pop(self):
#         if self.top==-1:
#             print("Stack is empty")
#         else:
#             value =self.stack[self.top]
#             self.stack[self.top]=None
#             self.top-=1
#             return value
          
   

# class Solution(object):
#     def removeStars(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         stack=Stack(len(s))
#         for i in s:
#             if i=="*":
#                 stack.pop()
#             else:
#                 stack.push(i)
#         outputstring=[item for item in stack.stack if item is not None]
#         return "".join(outputstring)


          
   

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        buff=[]
        for i in s:
            if i=="*":
                buff.pop()
            else:
                buff.append(i)
        outputstring=[item for item in buff if item is not None]
        return "".join(outputstring)
s="erahse*****"
instance = Solution()
print(instance.removeStars(s))