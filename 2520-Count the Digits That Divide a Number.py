class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count=0
        number=num
        while num!=0:
            rem=num%10
            if number%rem==0:
                count+=1
            num=num//10
        return count
        # count=0
        # for i in str(num):
        #     if num%int(i)==0:
        #         count+=1
        # return count