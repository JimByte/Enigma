alphabet = 'abcdefghijklmnopqrstuvwxyz'
RotorKey = 'dwebakxhzrnplyuqmjcstgivofgwutdzqlyckxapimvbnsorjehfhqcbuonrktefzvwidpxljsamyg'
text='hi'
def Reflector(R):
    return alphabet[(26-alphabet.find(R))-1]
def OneCharUp(R):
    R2 = []
    for i in range(25):
        i = i+1
        R2.append(R[i])
    R2.append(R[0])
    return R2
Cipher=''
R1 = list(RotorKey[0:26])
R2 = list(RotorKey[26:52])
R3 = list(RotorKey[52:78])
CR1 = 0
CR2 = 0
CR3 = 0
for i in text:
    E1 = R1[list(alphabet).index(i)]
    E2 = R2[list(alphabet).index(E1)]
    E3 = R3[list(alphabet).index(E2)]
    E4 = Reflector(E3)
    Cipher+=E4
    CR1 += 1
    R1 = OneCharUp(R1)
    R1
print(Cipher)
