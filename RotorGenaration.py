from random import shuffle 
alphabet = 'abcdefghijklmnopqrstuvwxyz'
Rotor1 = list(alphabet)
shuffle(Rotor1)
Rotor1 = ''.join(Rotor1)
Rotor2 = list(alphabet)
shuffle(Rotor2)
Rotor2 = ''.join(Rotor2)
Rotor3 = list(alphabet)
shuffle(Rotor3)
Rotor3 = ''.join(Rotor3)
f = open('./RotorLog.txt','w')
RotorKey = str(Rotor1+Rotor2+Rotor3)
f.write(RotorKey)
f.close()
