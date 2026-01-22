binary_number = "1010"  # Example binary number as a string
decimal_number = 0
power = 0

for digit in reversed(binary_number):  
    decimal_number += int(digit) * (2 ** power)  
    power += 1  

print(decimal_number)  # Output: 10
