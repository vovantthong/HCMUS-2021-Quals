# TestYourCmd
## Đề bài
Tác giả cho 1 file `Evidences.zip`

![Screenshot 2021-05-25 203410](https://user-images.githubusercontent.com/41907864/119506930-93f64100-bd98-11eb-8d41-f3bcfa9dcfa5.png)

## Hướng giải
- Giải nén file tác giả cho thì có khá nhiều file và thư mục, trong thư mục `.log` có rất nhiều thư mục và có 1 file hình `Master.png`
- Tuy nhiên không mở được, thử xem bằng phần mềm `HxD` thì rõ ràng mấy byte đầu đã bị chỉnh sửa

![Screenshot 2021-05-25 203309](https://user-images.githubusercontent.com/41907864/119506781-7032fb00-bd98-11eb-9cfb-87031d436368.png)

- Sửa lại các byte đầu bị sai, thu được 1 hint khác

![Master (2)](https://user-images.githubusercontent.com/41907864/119507358-f94a3200-bd98-11eb-9568-88d70773e9ca.png)

- Theo hint thì tiếp tục tìm các file có chứa chuỗi Ronaldo, phát hiện 1 vài file trong thư mục `.log` có chứa các bức thư bị `hex encode` và `base64 encode`, thu được `secret key` là `SuPer_Gold_3ymArJr.`

```python3
import glob
import binascii
import base64
import binascii

root_dir = '/mnt/c/Users/ADMIN/Desktop/HCMUS/Evidences/Evidences/.log/'
for filename in glob.iglob(root_dir + '**/**.log', recursive=True):
    with open(filename, 'rb') as f:
        content = f.read()
        if b'Send To: Ronaldo' in content and b'From: Messi' in content:
            content = content.split(b'Content: \n')[1].replace(b'\n', b'')
            try:
                print(binascii.unhexlify(content))
            except:
                print(base64.b64decode(content))
```
- Tiếp tục sử dụng steghide (theo hint từ hình `Master.png`) để extract data từ các hình trong thư mục `Secret` thu được flag

```python3
import glob
import binascii
from pwn import *
import base64
import subprocess
import binascii
import sys

root_dir = '/mnt/c/Users/ADMIN/Desktop/HCMUS/Evidences/Evidences/Secret/'
for filename in glob.iglob(root_dir + '**/**', recursive=True):
    p = process(['/usr/bin/steghide', "extract", "-sf", filename, "-p", "SuPer_Gold_3ymArJr.", "-xf", "cmd.txt"])
    print(p.recvall())
```

Flag: HCMUS-CTF{at_least_I_hope_you_can_code_a_bit}