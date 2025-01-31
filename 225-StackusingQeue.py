class Queue:
    def __init__(self,size):
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
        self.capacity=size
    
    def enqueue(self, value):
        if self.rear==self.capacity-1:
            print("Qeueue is filled")
        else:
            if self.front==-1:
                self.front=0
            self.rear+=1
            self.queue[self.rear]=value
    
    def dequeue(self):
        if self.front==-1:
            print("Qeueue is empty")
        else:
            value=self.queue[self.front]
            self.queue[self.front]=None
            self.front+=1
            if self.front>self.rear:
                self.front=self.rear=-1
            return value

    def peek(self):
        if self.isEmpty():
            print("Qeue is empty")
            return None
    
        return   self.queue[self.front]

    def isEmpty(self):
        return self.front==-1 or self.front>self.rear

    def isFull(self):  
        return self.rear==self.size-1

    def size(self):
        if self.isEmpty():
            return 0
        return self.rear-self.front+1

    def display(self):
        if self.isEmpty():
            print("Qeueue is empty")
        else:
            print("Qeueue elements:", self.queue[:self.rear + 1])

           



class MyStack(object):

    def __init__(self):
        self.queue1=Queue(10)
        self.queue2=Queue(10)

        
        
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue2.enqueue(x)
        while not self.queue1.isEmpty():
            self.queue2.enqueue(self.queue1.dequeue())
        self.queue1,self.queue2=self.queue2,self.queue1

        

    def pop(self):
        """
        :rtype: int
        """
        value= self.queue1.dequeue()
        return value
        
        

    def top(self):
        """
        :rtype: int
        """
        return self.queue1.peek()
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.queue1.isEmpty()   and self.queue2.isEmpty()
        

    
s=MyStack()
s.push(1)
s.push(2)
s.push(3)
print(s.top())
print(s.pop())
print(s.top())
print(s.pop())
print(s.pop())
print(s.empty())