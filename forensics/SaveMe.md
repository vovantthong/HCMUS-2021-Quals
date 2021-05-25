# Save me
## Đề bài
Tác giả cho 1 file `text` có nội dung khá giống hexdump, tuy nhiên bị mất 1 vài phần, được ngăn cách nhau bởi dấu `*`

```
0000010 2c01 0000 e1ff 6244 7845 6669 0000 4949
0000020 002a 0008 0000 0007 0112 0003 0001 0000
0000030 0001 0000 011a 0005 0001 0000 0062 0000
0000040 011b 0005 0001 0000 006a 0000 0128 0003
0000050 0001 0000 0002 0000 0131 0002 000d 0000
0000060 0072 0000 0132 0002 0014 0000 0080 0000
0000070 8769 0004 0001 0000 0094 0000 00a6 0000
0000080 012c 0000 0001 0000 012c 0000 0001 0000
0000090 4947 504d 3220 312e 2e30 3232 0000 3032
00000a0 3132 303a 3a34 3632 3120 3a30 3635 313a
00000b0 0033 0001 a001 0003 0001 0000 0001 0000
00000c0 0000 0000 0008 0100 0004 0001 0000 0100
00000d0 0000 0101 0004 0001 0000 00c0 0000 0102
00000e0 0003 0003 0000 010c 0000 0103 0003 0001
00000f0 0000 0006 0000 0106 0003 0001 0000 0006
0000100 0000 0115 0003 0001 0000 0003 0000 0201
0000110 0004 0001 0000 0112 0000 0202 0004 0001
0000120 0000 4347 0000 0000 0000 0008 0008 0008
0000130 d8ff e0ff 1000 464a 4649 0100 0001 0100
0000140 0100 0000 dbff 4300 0800 0606 0607 0805
0000150 0707 0907 0809 0c0a 0d14 0b0c 0c0b 1219
0000160 0f13 1d14 1f1a 1d1e 1c1a 201c 2e24 2027
0000170 2c22 1c23 281c 2937 302c 3431 3434 271f
0000180 3d39 3238 2e3c 3433 ff32 00db 0143 0909
0000190 0c09 0c0b 0d18 180d 2132 211c 3232 3232
00001a0 3232 3232 3232 3232 3232 3232 3232 3232
*
00001c0 3232 3232 3232 3232 3232 3232 3232 c0ff
00001d0 1100 0008 01c0 0300 2201 0200 0111 1103
00001e0 ff01 00c4 001f 0100 0105 0101 0101 0001
00001f0 0000 0000 0000 0100 0302 0504 0706 0908
0000200 0b0a c4ff b500 0010 0102 0303 0402 0503
0000210 0405 0004 0100 017d 0302 0400 0511 2112
```
## Hướng giải
- Theo dự đoán, code script tự động tạo 1 list có `size` bằng địa chỉ lớn nhất trong file `text`, sau đó parse từng dòng, lấy địa chỉ convert qua decimal sau đó gán 16 byte tương ứng của mỗi dòng vào đúng vị trí trong list
- Sau khi lấy tầm 100 byte đầu ra xem xét, thấy có khả năng đây chính là file hình `JPG`, tuy nhiên cứ 2 byte cạnh nhau lại bị tráo đổi vị trí, viết script để đổi lại vị trí các byte

```python
lines = open('text', 'rb').readlines()

print '[+] Length:', len(lines)

arr = ['\x00'] * 377942
for line in lines:
    line = line.strip('\n')
    if line == '*':
        print '[+] missing...'
    else:
        ps = line.split(' ')
        addr = int(ps[0], 16)
        del ps[0]
        for i in range(len(ps)):
            ps[i] = ps[i].decode('hex')[::-1].encode('hex')
        data = ''.join(ps).decode('hex')
        for i in range(len(data)):
            arr[addr + i] = data[i]
with open('result.jpg', 'wb') as f:
    f.write(''.join(arr))
```