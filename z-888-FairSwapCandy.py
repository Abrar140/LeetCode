class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        sumofAlice=sum(aliceSizes)
        sumofBob=sum(bobSizes)
        print(sumofAlice,sumofBob)
        average= sumofAlice/2 + sumofBob/2
        
        for  alice in aliceSizes:
            for bob in bobSizes:
                if alice+bob == sum(aliceSizes)/2 + sum(bobSizes)/2:
                    return [alice,bob]

            


aliceSizes = [2] 
bobSizes = [1,3]

print(Solution().fairCandySwap(aliceSizes, bobSizes))