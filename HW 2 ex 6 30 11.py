a = float(input('Type lenth in cm of first triange side and press enter:'))
b = float(input('Type lenth in cm of second triange side and press enter:'))
c = float(input('Type lenth in cm of third triange side and press enter:'))
p = (a+b+c)*0.5
s = ((p*(p-a)*(p-b)*(p-c)))**0.5
print('The area of triangle is:',s,'square cm.')