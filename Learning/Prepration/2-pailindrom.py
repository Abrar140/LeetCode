num= 12321
orignal=num
rev=0
while num!=0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev)
if orignal==num:
    print("yes")
else:
    print("no")