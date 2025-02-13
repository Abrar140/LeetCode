# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkList:
#     def __init__(self):
#         self.head = None

#     def insertlast(self,data):
#         newnode= Node(data)
#         if self.head is None:
#             self.head=newnode
#             return
#         temp=self.head
#         while temp.next:
#             temp=temp.next
#         temp.next=newnode



# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution(object):
#     def deleteDuplicates(self, head):
#         """
#         :type head: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         l2=LinkList()
#         temp=None
#         for i in range(len(head)):
#             if temp == None:
#                 l2.insertlast(head[i])
#                 temp=l2.head

#             if head[i]!=temp.data:
#                 l2.insertlast(head[i])
#                 temp=temp.next

#             return l2
        
#         l2.display()
        

# head = [1,1,2,3,3,4,4,4]
# sol=Solution()
# print(sol.deleteDuplicates(head))





















class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def insertlast(self,data):
        newnode= Node(data)
        if self.head is None:
            self.head=newnode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode

    def deletenode(self,key):
        temp=self.head
        if temp and temp.data==key:
            self.head=temp.next
            temp=None
            return
        prev=None
        while temp and temp.data!=key:
            prev=temp
            temp=temp.next
        if temp is None:
            return
        prev.next=temp.next
        temp=None
  
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        print(head.head.data)
        temp=head.head
        while temp:
            if temp.next is None:
                return head
            else:
               if  temp.next.data==temp.data:
                head.deletenode(temp.data)
                temp=temp.next
               else:
                temp=temp.next
        return head
        # l2=LinkList()
        # temp=None
        # for i in range(len(head)):
        #     if temp == None:
        #         l2.insertlast(head[i])
        #         temp=l2.head

        #     if head[i]!=temp.data:
        #         l2.insertlast(head[i])
        #         temp=temp.next

        #     return l2
        
        # l2.display()
        

head = [1,1,2,3,3,4,4,4]

l1=LinkList()
for i in range(len(head)):
    l1.insertlast(head[i])

l1.display()
head=l1

sol=Solution()
print(sol.deleteDuplicates(head))




class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head