print('BINARY TO OCTAL CONVERSION')
print('------------------------------')
print('\nBinary to OCTAL')
binStr = input('Give me a binary string: ')
temp = binStr
newOct = 0
power = 0
while len(temp) > 0:  
    bit = int(temp[-1])  
    newOct = newOct + bit * 8 ** power  
    temp = temp[:-1]  
    power += 1  
print("The binary number " + binStr, 'as an integer is', newOct)
print('------------------------------')
