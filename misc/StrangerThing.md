# StrangerThing
Kết nối ssh tới server `ssh ctf@61.28.237.24  -p 3040`

Phát hiện có 3 file `flag1.txt`, `flag-2.txt` và `secret/.flag3.txt`

Với `flag1.txt` thì chỉ cần dùng lệnh `cat flag1.txt`

Với file `flag-2.txt` thì do có kí tự `-` nên cần phải dùng 1 kỹ thuật để bypass `cat < 'flag-2.txt'`

Còn file `.flag3.txt` thì với lệnh `ls` thì sẽ không hiện ra, phải dùng lệnh `ls -la` để xem mới thấy file

Sau khi lấy được 3 phần của flag, ghép lại thu được flag