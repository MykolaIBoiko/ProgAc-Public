n = int(input("Enter number:"))
s = 0
while n > 0:
    d = n % 10
    s = s+d
    n = n//10
print('Sum of digits in number is', s)