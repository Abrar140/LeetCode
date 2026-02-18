class Solution(object):
    def rotate(self, matrix):

        print(len(matrix)//2)
       
        # print("Output is ...[7,4,1],[8,5,2],[9,6,3]]")
        print("Output is ..... [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]")

        for i in range(len(matrix)//2+1):

            temp = matrix[i][0]
            matrix[i][0] = matrix[len(matrix)-1-i][i]
            matrix[len(matrix)-1-i][i] = matrix[len(matrix)-1-i][len(matrix)-1-i]
            matrix[len(matrix)-1-i][len(matrix)-1-i] = matrix[i][len(matrix)-1-i]
            matrix[i][len(matrix)-1-i] = temp

        #     print(matrix)
        # #   for j in range(len(matrix[i])):
        # #     print("i=",i,"j=",j,"len(matrix)-i-1=",len(matrix)-i-1,"len(matrix)-j-1=",len(matrix)-j-1,"matrix[i][j]",matrix[i][j],"matrix[j][len(matrix)-i-1]",matrix[j][len(matrix)-i-1])
        # #     matrix[i][j], matrix[j][len(matrix)-i-1]=matrix[j][len(matrix)-i-1] ,matrix[i][j]
        # print(matrix)
            
        return matrix




matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution = Solution()
print(solution.rotate(matrix))





# class Solution(object):
#     def rotate(self, matrix):
#         n = len(matrix)
        
#         for layer in range(n // 2):
#             first = layer
#             last = n - 1 - layer
#             for i in range(first, last):
#                 offset = i - first
#                 top = matrix[first][i]
                
#                 # left -> top
#                 matrix[first][i] = matrix[last - offset][first]

#                 # bottom -> left
#                 matrix[last - offset][first] = matrix[last][last - offset]

#                 # right -> bottom
#                 matrix[last][last - offset] = matrix[i][last]

#                 # top -> right
#                 matrix[i][last] = top

#         return matrix

# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# # matrix = [[1,2,3],[4,5,6],[7,8,9]]
# solution = Solution()
# print(solution.rotate(matrix))