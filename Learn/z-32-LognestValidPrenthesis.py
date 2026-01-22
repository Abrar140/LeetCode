class Stack:
    def __init__(self, size):
        self.stack=[None]*size
        self.top=-1
        self.size=size
    
    def push(self, value):
        if self.top==self.size-1:
            print ("Stack is full")
        else:
            self.top+=1
            self.stack[self.top]=value

    def pop(self):
        if self.top==-1:
            print("Stack is empty")
        else:
            value =self.stack[self.top]
            self.stack[self.top]=None
            self.top-=1
            return value
          
    def peek(self):
        if self.top == -1:
            print("Stack is empty")
            return None
        else:
            return self.stack[self.top]

    def isEmpty(self):
        return self.top == -1

   


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=Stack(len(s))
        count=0
        max=0
        for i in s:
            if i=='(':
                stack.push(i)
                count+=1
            elif i==')':
                if stack.peek()=='(':
                    count+=1 
                    stack.pop()
                    if max<count:
                        max=count
                        count=0
                    else:
                        max=max
                        
                    
        if stack.isEmpty():
            return count
        else:
            return count-(stack.top+1)


        

s="()(()"
sol= Solution()
print(sol.longestValidParentheses(s))