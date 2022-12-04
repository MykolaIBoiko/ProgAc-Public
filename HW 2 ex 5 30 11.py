a = int(input('Type 3 digit number:'))
b = a % 10
c = a % 100//10
d = a//100
e = b+c+d
print('Sum of numbers digits are:', e)