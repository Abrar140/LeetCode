
class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue=[None]*k
        self.front=-1
        self.rear=-1
        self.capacity=k
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        
        if self.front==0:
            return False
        else: 
            if self.front==-1:
                self.front=self.rear=0
            else:
                    self.front-=1
            self.queue[self.front]=value
            return True
        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.rear==self.capacity-1:
            return False
        else:
            if self.front==-1:
                self.front=self.rear=0
            else:
                self.rear+=1
            self.queue[self.rear]=value
            return True
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.front==-1:
            return False
        else:
            value=self.queue[self.front]
            self.queue[self.front]=None
            self.front+=1
            if self.front>self.rear:
                self.front=self.rear=-1
            return True
        

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.rear==-1:
            return False
        else:
            value=self.queue[self.rear]
            self.queue[self.rear]=None
            self.rear-=1
            if self.front>self.rear:
                self.front=self.rear=-1
            return True
        

    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.front]
        

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.front==-1 or self.front>self.rear
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.rear==self.capacity-1
        