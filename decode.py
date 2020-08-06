alphabet = 'abcdefghijklmnopqrstuvwxyz'
RotorKey = 'dwebakxhzrnplyuqmjcstgivofgwutdzqlyckxapimvbnsorjehfhqcbuonrktefzvwidpxljsamyg'
Cipher = 'qgizscfplgzto'
Plain = ''
R1 =list(RotorKey[0:26])
R2 =list(RotorKey[26:52])
R3 =list(RotorKey[52:78])
def Reflector(R):
    return alphabet[(26-alphabet.find(R))-1]
def OneCharDown(R):
    R2 = []
    R2.append(R[25])
    for i in range(25):
        R2.append(R[i])
    return R2
def OneCharUp(R):
    R2 = []
    for i in range(25):
        i = i+1
        R2.append(R[i])
    R2.append(R[0])
    return R2

CR1 = 0
CR2 = 0
CR3 = 0
for i in range(len(Cipher)-1):
    R1 = OneCharUp(R1)
    CR1 += 1
    if CR1 == 26:
        R2 = OneCharUp(R2)
        CR1 = 0
        CR2 += 1
    if CR2 == 26:
        R3 = OneCharUp(R3)
        CR2 = 0
        CR3 += 1

CR1 = 0
CR2 = 0
CR3 = 0
for i in Cipher[::-1]:
    R1 = ''.join(R1)
    R2 = ''.join(R2)
    R3 = ''.join(R3)
    I4 = Reflector(i)
    I3 = alphabet[R3.find(I4)]
    I2 = alphabet[R2.find(I3)]
    I1 = alphabet[R1.find(I2)]
    Plain+=I1
    R1 = OneCharDown(R1)
    CR1 += 1
    if CR1 == 26:
        R2 = OneCharDown(R2)
        CR1 = 0
        CR2 += 1
    if CR2 == 26:
        R3 = OneCharDown(R3)
        CR2 = 0
        CR3 += 1
Plain = Plain[::-1]
print(Plain)
