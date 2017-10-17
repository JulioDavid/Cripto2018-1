# Affine Cipher
 2. # http://inventwithpython.com/hacking (BSD Licensed)
 3.
 4. import sys, pyperclip, cryptomath, random
 5. SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~""" # note the space at the front
 6.
 7.
 8. def main():
 9.     myMessage = """"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing"""
10.     myKey = 2023
11.     myMode = 'encrypt' # set to 'encrypt' or 'decrypt'
12.
13.     if myMode == 'encrypt':
14.         translated = encryptMessage(myKey, myMessage)
15.     elif myMode == 'decrypt':
16.         translated = decryptMessage(myKey, myMessage)
17.     print('Key: %s' % (myKey))
18.     print('%sed text:' % (myMode.title()))
19.     print(translated)
20.     pyperclip.copy(translated)
21.     print('Full %sed text copied to clipboard.' % (myMode))
22.
23.
24. def getKeyParts(key):
25.     keyA = key // len(SYMBOLS)
26.     keyB = key % len(SYMBOLS)
27.     return (keyA, keyB)
28.
29.
30. def checkKeys(keyA, keyB, mode):
31.     if keyA == 1 and mode == 'encrypt':
32.         sys.exit('The affine cipher becomes incredibly weak when key A is set to 1. Choose a different key.')
33.     if keyB == 0 and mode == 'encrypt':
34.         sys.exit('The affine cipher becomes incredibly weak when key B is set to 0. Choose a different key.')
35.     if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
36.         sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
37.     if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
38.         sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, len(SYMBOLS)))
39.
40.
41. def encryptMessage(key, message):
42.     keyA, keyB = getKeyParts(key)
43.     checkKeys(keyA, keyB, 'encrypt')
44.     ciphertext = ''
45.     for symbol in message:
46.         if symbol in SYMBOLS:
47.             # encrypt this symbol
48.             symIndex = SYMBOLS.find(symbol)
49.             ciphertext += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
50.         else:
51.             ciphertext += symbol # just append this symbol unencrypted
52.     return ciphertext
53.
54.
55. def decryptMessage(key, message):
56.     keyA, keyB = getKeyParts(key)
57.     checkKeys(keyA, keyB, 'decrypt')
58.     plaintext = ''
59.     modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))
60.    
61.     for symbol in message:
62.         if symbol in SYMBOLS:
63.             # decrypt this symbol
64.             symIndex = SYMBOLS.find(symbol)
65.             plaintext += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
66.         else:
67.             plaintext += symbol # just append this symbol undecrypted
68.     return plaintext
69.
70.
71. def getRandomKey():
72.     while True:
73.         keyA = random.randint(2, len(SYMBOLS))
74.         keyB = random.randint(2, len(SYMBOLS))
75.         if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
76.             return keyA * len(SYMBOLS) + keyB
77.
78.
79. # If affineCipher.py is run (instead of imported as a module) call
80. # the main() function.
81. if __name__ == '__main__':
82.     main()