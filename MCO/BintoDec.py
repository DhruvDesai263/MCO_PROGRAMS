print('BINARY TO DECIMAL CONVERSION')
print('------------------------------')
print('\nBinary to Decimal')
binStr = input('Give me a binary string: ')
temp = binStr
newInt = 0
power = 0
while len(temp) > 0:  
    bit = int(temp[-1])  
    newInt = newInt + bit * 2 ** power  
    temp = temp[:-1]  
    power += 1  
print("The binary number " + binStr, 'as an integer is', newInt)
print('------------------------------')
