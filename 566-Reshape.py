class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        output=[]
        result=[]
        if len(mat) * len(mat[0]) != r * c:
            return mat
        else:
             for i in range (len(mat)):
                for j in range (len(mat[0])):
                    output.append(mat[i][j]) 

             print(output)

             for  i in range(r):
                result.append([])
                for j in range(c):
                      result[i].append(output[i*c+j])

             return result

        # return result


            # return [mat[i][j] for i in range(len(mat)) for j in range(len(mat[0]))]

           

            # return output


        



mat = [[1,2],[3,4]]
r = 1
c = 4

Solution=Solution()
print(Solution.matrixReshape(mat, r, c))