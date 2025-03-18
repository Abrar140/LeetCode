class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        output=[]
        if k==0:
            return [0]*len(code)
        if k>0:
            for i in range(len(code)):
                sum=0
                d=i+1
                for j in range(k):
                    d= d%len(code)
                    sum+=code[d]
                    d+=1
                output.append(sum)
                sum=0
        else:
            for i in range(len(code)):
                sum=0
                d=i-1
                for j in range(abs(k)):
                    d= d%len(code)
                    sum+=code[d]
                    d-=1
                output.append(sum)
                sum=0
        
        return output



        

code = [2,4,9,3]
k = -2
sol=Solution()
print(sol.decrypt(code,k))






