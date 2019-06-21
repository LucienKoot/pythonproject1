# whilel loop,  prompt

tekstregels = list()
print('Type een tekstregel.')
print('Type "sluiten" om af te sluiten')
 
line = input('Je 1e tekstregel: ')
while line != 'sluiten':
    tekstregels.append(line)
    line = input('Volgende tekstregel: ')
 
print('Je tekstregels waren:')
for line in tekstregels:
    print(line)

