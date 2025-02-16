class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        outputarray=[]
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i]>prices[j]:
                    outputarray.append(prices[i]-prices[j])
                    break
                if j==len(prices)-1:
                    outputarray.append(prices[i])

            if i==len(prices)-1:
                outputarray.append(prices[i])

                
           
        return outputarray




prices = [8,4,6,2,3]
solution = Solution()
print(solution.finalPrices(prices))