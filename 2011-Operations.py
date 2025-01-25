class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        X=0
        for  x in operations:
            if x=="++X" or x=="X++":
                X=X+1
            else:
                X=X-1
        return X
        

operations = ["X++","++X","--X","X--"]
instance=Solution()
print( "The Output after Operation are",instance.finalValueAfterOperations(operations))
