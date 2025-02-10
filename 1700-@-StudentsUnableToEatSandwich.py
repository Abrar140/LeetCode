
# class Solution(object):
#     def countStudents(self, students, sandwiches):
#         """
#         :type students: List[int]
#         :type sandwiches: List[int]
#         :rtype: int
#         """
#         q=[]
#         for i in range(len(students)):
#             q.append(students[i])
        
#         while sandwiches:
#             if q[0]==sandwiches[0]:
#                 q.pop(0)
#                 sandwiches.pop(0)
#             else:
#                 elem=q.pop(0)
#                 q.append(elem)
        
#         return len(q)
        


# students = [1,1,0,0]
# sandwiches = [0,1,0,1]

# print(Solution().countStudents(students, sandwiches))








class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count0=students.count(0)
        count1=students.count(1)

        for s in sandwiches:
            if s==0 and count0>0:
                count0-=1
            elif s==1 and count1>0:
                count1-=1
            else:
                break
        return count0+count1
      
students = [1,1,0,0]
sandwiches = [0,1,0,1]

print(Solution().countStudents(students, sandwiches))








        
        