# class Solution(object):
#     def timeRequiredToBuy(self, tickets, k):
#         """
#         :type tickets: List[int]
#         :type k: int
#         :rtype: int
#         """
#         count=0
#         while tickets[k]>0:
#             for i in range (len(tickets)-1):
#                 if tickets[i]>0:
#                     tickets[i]-=1
#                     count+=1
#                 if tickets[i]==0:
#                     if tickets[k]==0:
#                         return count
#                     tickets.pop(i)
#                     if k>0:
#                       k=k-1
#                 print(tickets,k,count)

                
#         return count




class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        while tickets[k]>0:
            for i in range (len(tickets)):
                if tickets[i]>0:
                    tickets[i]-=1
                    count+=1
                if tickets[k]==0 and i==k:
                    return count
      



tickets =[2,3,2]
k = 2
# tickets = [84,49,5,24,70,77,87,8]
# k = 3
sol=Solution()
print(sol.timeRequiredToBuy(tickets,k))