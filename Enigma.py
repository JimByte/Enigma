alphabet = 'abcdefghijklmnopqrstuvwxyz'
def Rotate(c):
    return c[-1]+c[0:-1]
def Reflector(c):
    return alphabet[(26-alphabet.find(c))-1]
def Enigma(Plain_Cipher,Key):
    Cipher = ''
    State = 0
    K1 =Key[0:26]
    K2 =Key[26:52]
    K3 =Key[52:78]
    for i in Plain_Cipher:
        State+=1
        In1 = K1[alphabet.find(i)]
        In2 = K2[alphabet.find(In1)]
        In3 = K3[alphabet.find(In2)]
        Re0 = Reflector(In3)
        Ou3 = alphabet[K3.find(Re0)]
        Ou2 = alphabet[K2.find(Ou3)]
        Ou1 = alphabet[K1.find(Ou2)]
        Cipher += Ou1
        K1 = Rotate(K1)
        if State%26==0:
            K2 = Rotate(K2)
        if State%675==0:
            K3 = Rotate(K3)
    return Cipher
def KeyGenaration():
    from random import shuffle
    Rotor1 = list(alphabet)
    shuffle(Rotor1)
    Rotor1 = ''.join(Rotor1)
    Rotor2 = list(alphabet)
    shuffle(Rotor2)
    Rotor2 = ''.join(Rotor2)
    Rotor3 = list(alphabet)
    shuffle(Rotor3)
    Rotor3 = ''.join(Rotor3)
    return str(Rotor1+Rotor2+Rotor3)
inp=''
while inp!='0':
    print('-->  Welcome To Enigma  <--'.center(100))
    print('Use this command : \n T ----> TRANSLATE \n K ----> NEW KEY \n 0 ----> EXIT')
    inp = input("Type your order : ")
    if inp=='T' or inp=='t':
        PlainCipher = input('Input Your Plain or Cipher : ')
        Key = input('Input Your Enigma Key :')
        print(Enigma(PlainCipher, Key))
    if inp=='K' or inp=='k':
        print('Save Your key --->  '+KeyGenaration())
    print('-------------------------------------------------------------------------------------')
