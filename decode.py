alphabet = 'abcdefghijklmnopqrstuvwxyz'
RotorKey = 'dwebakxhzrnplyuqmjcstgivofgwutdzqlyckxapimvbnsorjehfhqcbuonrktefzvwidpxljsamyg'
Input = 'qgizs'
Output = ''
R1 = list(RotorKey[0:26])
R2 = list(RotorKey[26:52])
R3 = list(RotorKey[52:78])
CR1 = 0
CR2 = 0
CR3 = 0
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

for i in Input:
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
for i in Input[::-1]:
    I3 = list(alphabet)[R3.index(Reflector(i))]
    I2 = list(alphabet)[R2.index(I3)]
    I1 = list(alphabet)[R1.index(I2)]
    R1 = OneCharDown(R1)
    Output+=I1

print(Output[::-1])


