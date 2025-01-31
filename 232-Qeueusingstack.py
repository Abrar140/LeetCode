class Stack:
    def __init__(self, size):
        self.stack=[None]*size
        self.top=-1
        self.size=size
    
    def push(self, value):
        if self.top==self.size-1:
            print ("Stack is full")
            return
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

   








class MyQueue(object):

    

    def __init__(self):
        self.stack1=Stack(10)
        self.stack2=Stack(10)
      
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.push(x)
        
        

    def pop(self):
        """
        :rtype: int
        """
        while not self.stack1.isEmpty():
            self.stack2.push(self.stack1.pop())
        
        popout=self.stack2.pop()
        while not self.stack2.isEmpty():
            self.stack1.push(self.stack2.pop())
        return popout
        

    def peek(self):
        """
        :rtype: int
        """

        while not self.stack1.isEmpty():
            self.stack2.push(self.stack1.pop())
        
        peekelement=self.stack2.peek()
        while not self.stack2.isEmpty():
            self.stack1.push(self.stack2.pop())
        return peekelement
        
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.stack1.isEmpty() and self.stack2.isEmpty()
            
        

q=MyQueue()
q.push(1)
q.push(2)
q.push(3)
print(q.peek())
print(q.pop())
print(q.pop())
print(q.empty())
print(q.pop())
print(q.empty())