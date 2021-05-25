# Memory
Tác giả cho file `memory.raw`, theo tên bài là memory nên thử dùng volatility để chọc phá coi bên trong có gì
Thử kiểm tra thông tin của file bằng lệnh `volatility -f memory.raw imageinfo`
![Screenshot 2021-05-25 224816](https://user-images.githubusercontent.com/41907864/119528353-50590280-bdab-11eb-8b9c-470b713f4e37.png)
Sử dụng profile `Win7SP1x64` kiểm tra `Consoles`
```
Microsoft Windows [Version 6.1.7601]                                            
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.                 
                                                                                
C:\Users\Test>You should get the flag online                                    
'You' is not recognized as an internal or external command,                     
operable program or batch file.                                                 
                                                                                
C:\Users\Test>But here is the first part of the encryption key: SuP3r_          
'But' is not recognized as an internal or external command,                     
operable program or batch file.                                                 
                                                                                
C:\Users\Test>
```
Thu được phần đầu của key `SuP3r_` và nhận được hint phải tìm flag online
Tiếp tục check các process đang chạy bằng module pslist
![Screenshot 2021-05-25 225153](https://user-images.githubusercontent.com/41907864/119528926-d1b09500-bdab-11eb-929f-8deeaa3bdca9.png)
Nhận thấy máy tác giả đang mở chrome, tuy nhiên cần phải dùng plugin chrome để có thể xem được lịch sử, downloads,...
![Screenshot 2021-05-25 225426](https://user-images.githubusercontent.com/41907864/119529306-2e13b480-bdac-11eb-9fbf-039634cdfb6c.png)
Sau khi xem lịch sử trình duyệt thì phát hiện thấy tác giả đã truy cập vào 1 file trên google drive, có tên là `flag.zip`, tải file này về thì yêu cầu nhập mật khẩu, tuy nhiên ở bước trên chỉ mới có được 1 phần của mật khẩu, nên cần phải tìm kiếm thêm.
Tiếp tục tìm kiếm các file có đuôi đặc biệt, ví dụ `.txt` bằng lệnh sau `volatility -f memory.raw --profile Win7SP1x64 filescan | grep .txt`, phát hiện có file `flag.txt.txt` có địa chỉ sau `0x000000001e903f20      2      0 RW-r-- \Device\HarddiskVolume2\Users\Test\Desktop\flag.txt.txt`
Tiếp tục dump file này ra bằng lệnh `volatility -f memory.raw --profile=Win7SP1x64 dumpfiles -Q 0x000000001e903f20 -D .`, thu được file có nội dung sau `Second part of secret_key: P@zzw0rD`
Vậy là đã có đủ 2 phần của mật khẩu file zip, giải nén file `flag.zip` thu được flag
Flag: HCMUS-CTF{simple_memory_forensics_stuff}