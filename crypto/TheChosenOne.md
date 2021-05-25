# TheChosenOne
Tác giả cho source của server:
```python
#!/usr/bin/env python

from Crypto.Cipher import AES
from select import select
import sys

def padding(plaintext):

    plaintext_length = len(plaintext)
    padding_length = 0
    
    if plaintext_length % 32 != 0:
        padding_length = (plaintext_length // 32 + 1) * 32
    else:
        padding_length = 0
    return padding_length

def main():
    flag = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # TODO 
    key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # TODO
    
    padding_character = "D"
    
    assert (len(flag) == 32) and (len(key) == 32)
    cipher = AES.new(key, AES.MODE_ECB)

    banner = """
 _   _  ____ __  __ _   _ ____         ____ _____ _____
| | | |/ ___|  \/  | | | / ___|       / ___|_   _|  ___|
| |_| | |   | |\/| | | | \___ \ _____| |     | | | |_
|  _  | |___| |  | | |_| |___) |_____| |___  | | |  _|
|_| |_|\____|_|  |_|\___/|____/       \____| |_| |_|

"""
    sys.stdout.write(banner)
    sys.stdout.write("Welcome to AES-ECB Encryption Machine. \nPlease give us your plaintext, we'll give you its ciphertext!!!!")
    sys.stdout.write("\n=====================================\n")
    sys.stdout.flush()

    while True:
        try:
            sys.stdout.write('\nYour input: ')
            sys.stdout.flush()

            rlist, _, _ = select([sys.stdin], [], [])

            inp = ''
            if rlist:
                user_input = sys.stdin.readline().rstrip('\n')

            plaintext = user_input + flag
            padding_length = padding(plaintext)
            plaintext = plaintext.ljust(padding_length, padding_character)
            
            sys.stdout.write('The ciphertext:\n{}\n\n'.format((cipher.encrypt(plaintext)).encode('hex')))
        except KeyboardInterrupt:
            exit(0)   

if __name__ == '__main__':
    main()
```

Tác giả sử dụng thuật toán mã hóa `AES` mode `ECB`, sau khi nhận input nhập từ người dùng thì append thêm flag vào sau input, sau đó thêm padding `D` và mã hóa bằng thuật toán trên

Thuật toán mã hóa này có thể sử dụng kỹ thuật `known plaintext attack` để tìm ra flag

```python
#!/usr/bin/python

import math
import socket
import sys
from pwn import *

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def roundup(x, base=10):
    return int(math.ceil(x / (base + 0.0))) * base

r = remote('61.28.237.24', 30300)

try:
    found = False
    secret = ""

    secretLen = 0
    #prependChars = "ENCRYPT:"
    prependChars = ""

    message = "A"
    r.recvuntil('Your input:')
    r.sendline(message)
    r.recvuntil('The ciphertext:')
    r.recvline()
    data = r.recvline()
    output = list(chunkstring(data, 32))
    initialLen = len(output)

    curLen = 0

    while (curLen <= initialLen):
        message += "A"
        r.recvuntil('Your input:')
        r.sendline(message)
        r.recvuntil('The ciphertext:')
        r.recvline()
        data = r.recvline()
        output = list(chunkstring(data, 32))
        curLen = len(output)

    extra = len(message) - 1

    secretLen = ((curLen - 1) * 16) - extra - len(prependChars)

    print "SECRETLEN: " + str(secretLen)

    while not found:
        initialBlock = "A" * (16 - len(prependChars))
        fullLen = roundup(secretLen, 16)
        prepend = "B" * (fullLen - len(secret) - 1)
        message1 = initialBlock + prepend

        r.recvuntil('Your input:')
        r.sendline(message1)
        r.recvuntil('The ciphertext:')
        r.recvline()
        data = r.recvline()
        initialReturn = list(chunkstring(data, 32))
        print "INITIAL: " + str(initialReturn)

        for i in range(33, 127):
            message2 = message1 + secret + chr(i)
            r.recvuntil('Your input:')
            r.sendline(message2)
            r.recvuntil('The ciphertext:')
            r.recvline()
            data = r.recvline()
            oracle = list(chunkstring(data, 32))
            #print "ORACLE: " + str(oracle)
            compareBlock = (len(prependChars + message2) / 16) - 1
            #print "COMPARE = " + str(compareBlock)
            if oracle[compareBlock] == initialReturn[compareBlock]:
                secret += chr(i)
                print "LENGTH: " + str(len(secret))
                print "SECRET: " + secret
                print "INITIAL: " + str(initialReturn)
                print "ORACLE: " + str(oracle)
                if len(secret) == secretLen:
                    found = True
                    print secret
                break
    
finally:
    r.close()
```

Sau khi chạy script để attack thì thu được flag: HCMUS-CTF{You_Can_4ttack_A3S!?!}