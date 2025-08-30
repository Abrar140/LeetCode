class Solution(object):
    def date_to_binary(self, date):
        year, month, day = map(int, date.split('-'))
        return f"{bin(year)[2:]}-{bin(month)[2:]}-{bin(day)[2:]}"





date = "2080-02-29"
print(Solution().date_to_binary(date))