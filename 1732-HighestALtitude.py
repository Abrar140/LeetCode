class Solution(object):
    def largestAltitude(self, gain):
        max=0
        current=0
        for  x in gain:
            current=current+x
            if current>max:
                max=current
        return max
           
gain = [-4,-3,-2,-1,4,3,2] 
instance=Solution()
print( "The maximum gain is ",instance.largestAltitude(gain))          