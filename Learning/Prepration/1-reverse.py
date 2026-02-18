def reverse_integer(n):
    is_negative = n < 0
    n = abs(n)
    reversed_num = 0
    
    while n != 0:

        digit = n % 10
        # print(digit)
        reversed_num = reversed_num * 10 + digit
        n //= 10
        print("......",reversed_num,n)

    if is_negative:
        reversed_num *= -1
    
    return reversed_num

print(reverse_integer(12345))  # Output: 54321
print(reverse_integer(-9876))  # Output: -6789
