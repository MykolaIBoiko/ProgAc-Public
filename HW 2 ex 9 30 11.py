a = int(input('Enter number:'))
b = 0
while a > 0:
    c = a % 10
    a = a // 10
    b = b * 10
    b = b + c
print('Inverse number to the entered number is:', b)


