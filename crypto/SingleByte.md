# SingleByte
Tác giả cho 1 chuỗi `base64` như sau `r4SJmJOanoOFhMqDmcqLyp2Lk8qFjMqZiZiLh4iGg4SNyo6LnovKmYXKnoKLnsqFhIaTyoufnoKFmIOQj47KmouYnoOPmcqJi4TKn4SOj5iZnouEjsqego/Kg4SMhZiHi56DhYTEyqOEyp6PiYKEg4mLhsqej5iHmcbKg57Kg5nKnoKPypqYhYmPmZnKhYzKiYWEnI+YnoOEjcqCn4eLhMeYj4uOi4iGj8qahouDhJ6Pkp7KnoXKg4SJhYeamI+Cj4SZg4iGj8qej5KexsqLhpmFyoGEhZ2EyouZyomDmoKPmJ6Pkp6iqae/ucepvqyRnY+1gYSFnbWegouetZOFn7WJi4S1joW1mYOHmoaPtbKluLXf3tnb2dvf3ouIiYyP396LjNiPiYuIlw==`

Decode chuỗi ban đầu thu được `298` byte

Vì đề bài có nói là `SingleByte` nên dự đoán tác giả đã dùng `xor` encode với key là 1 byte

Thử brute key cho đến khi chuỗi nhận được có dạng `HCMUS` thì thu được kết quả sau

![Screenshot 2021-05-25 233312](https://user-images.githubusercontent.com/41907864/119535349-13dcd500-bdb2-11eb-9ccf-51ab8733d6e7.png)

Flag: HCMUS-CTF{we_know_that_you_can_do_simple_XOR_54313154abcfe54af2ecab}