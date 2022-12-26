print('------------------------------')
print('DECIMAL TO BINARY CONVERSION')
print('Decimal to binary')
intStr = int(input('Give me an Decimal: '))
myInt = int(intStr)
binStr = ''
while myInt > 0:
    binStr = str(myInt % 2) + binStr
    myInt //= 2
    
print('The binary of', intStr, 'is', binStr)
print('------------------------------')

