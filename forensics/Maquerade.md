# Maquerade
- Tác giả cho 1 file `mitm.pcap`, vì tác giả có nói quá trình giao tiếp không mã hóa nên thử lọc protocol theo `http` liền
![Screenshot 2021-05-25 222357](https://user-images.githubusercontent.com/41907864/119524553-f145be80-bda7-11eb-8df9-079425ff5383.png)
- Phát hiện tác giả truy cập 3 file, sử dụng tính năng `Export Object -> HTTP` để export 3 file này
![Screenshot 2021-05-25 222910](https://user-images.githubusercontent.com/41907864/119525392-a8dad080-bda8-11eb-851c-d313c359ea9e.png)
- File `secret.zip` được đặt mật khẩu, nên chuyển qua việc đi tìm mật khẩu, file `CheckPass.class` là 1 file có info như sau `CheckPass.class: compiled Java class data, version 55.0`, nên phải dùng tool jdgui để decompiler source code. Thu được code như sau:
```java
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public class CheckPass {
  public static void main(String[] paramArrayOfString) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Please enter the password!!");
    String str1 = scanner.nextLine();
    if (str1.length() != 8) {
      System.out.println("Oops!!");
      return;
    } 
    if (!str1.substring(0, 6).matches("[0-9]+")) {
      System.out.println("Oops!!");
      return;
    } 
    if (!str1.substring(0, 1).equals(str1.substring(5, 6))) {
      System.out.println("Oops!!");
      return;
    } 
    if (!str1.endsWith("}")) {
      System.out.println("Oops!!");
      return;
    } 
    String str2 = "(?![@',&])\\p{Punct}";
    if (!str1.substring(6, 7).matches(str2)) {
      System.out.println("Oops!!");
      return;
    } 
    if (!getMd5(str1).equals("53e443c9f65cd5f816452ae66ec65834")) {
      System.out.println("Oops!!");
      return;
    } 
    System.out.println("You get the second part!!!");
  }
  
  public static String getMd5(String paramString) {
    try {
      MessageDigest messageDigest = MessageDigest.getInstance("MD5");
      byte[] arrayOfByte = messageDigest.digest(paramString.getBytes());
      BigInteger bigInteger = new BigInteger(1, arrayOfByte);
      String str = bigInteger.toString(16);
      while (str.length() < 32)
        str = "0" + str; 
      return str;
    } catch (NoSuchAlgorithmException noSuchAlgorithmException) {
      throw new RuntimeException(noSuchAlgorithmException);
    } 
  }
}
```
- Do `md5` này không được crack sẵn, nên phải dựa vào source, tự code lại để brute và tuân theo các điều kiện ở trên
    * password phải có 8 kí tự
    * Kết thúc bằng kí tự `}`
    * 6 ký tự đầu là số
    ...
- Sau khi brute thì thu được password là `897268$}`
- Sử dụng mật khẩu này để giải nén file `secret.zip` ban đầu, và thu được file `Part1.txt` có nội dung như sau `HCMUS-CTF{Just_Network_Stuff_`
- Kết hợp lại thu được flag: HCMUS-CTF{Just_Network_Stuff_897268$}