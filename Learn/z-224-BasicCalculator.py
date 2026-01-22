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

    def isFull(self):
        return self.top == self.size - 1

    def size(self):
        return self.top + 1

    def display(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Stack elements:", self.stack[:self.top + 1])

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=Stack(len(s))
        for index, i in enumerate(s):
            if i in ")}]":
                print(i)
            else:
              stack.push(i)
        while(stack.isEmpty()):
            element2=int(stack.pop())
            operator=stack.pop()
            element=int(stack.pop())
            
            print(x)

        return stack.stack
        #     print(stack.stack)
        #     if i !=" ":
        #         if i in ")}]":
                       
        #                 element2=int(stack.pop())#11
        #                 if stack.isEmpty():
        #                     stack.push(str(element2))
        #                     continue
        #                 operator=stack.pop() #(
        #                 if operator in "({[" and stack.isEmpty():
        #                     if index==len(s)-1:
        #                         return element2 
        #                     # else:
        #                     #     continue      
        #                 else:
        #                     if operator in "({[":
        #                        stack.push(str(element2))
        #                        element2=int(stack.pop())
        #                        operator=stack.pop()
                            
                            
        #                     element=int(stack.pop())
        #                     if stack.isEmpty==False:
        #                       bracket=stack.pop()
        #                       if  bracket not in "({[" :
        #                           stack.push(bracket)
        #                     # print("i am here ",operator, bracket, element,element2)

                           
        #                     if operator=="+":
        #                      stack.push(str(element+element2))
        #                     elif operator=="-":
        #                      stack.push(str(element-element2))
        #                     elif operator=="*":
        #                      stack.push(str(element*element2))
        #                     elif operator=="/":
        #                      stack.push(str(int(element/element2)))
                       
  
        #         else:

        #             peekelement=stack.peek()
        #             if peekelement != None and peekelement in "+-*/" and i not in "({[":
        #                 operator=stack.pop()
        #                 element=int(stack.pop())
        #                 if operator=="+":
        #                     stack.push(str(element+int(i)))
        #                 elif operator=="-":
        #                     stack.push(str(element-int(i)))
        #                 elif operator=="*":
        #                     stack.push(str(element*int(i)))
        #                 elif operator=="/":
        #                     stack.push(str(int(element/int(i))))
        #             else:
        #                 stack.push(i)

        # return int(stack.pop())
                 


                


s="2+3"
sol=Solution()
print(sol.calculate(s))