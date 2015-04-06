## Chương 2: Variables, expressions and statements
- Chương này sẽ giới thiệu với người đọc các kiến thức về `biến, biểu thức và các câu lệnh`

* [I. Ghi chép chương 2](#ghichepchuong2)
* [2.1. Giá trị và các kiểu của nó](#2.1)
* [2.2. Biến - `variables` trong python](#2.2)
* [2.3. Tên của biến và các từ khóa trong python](#2.3)
* [2.4. Toán tử (`operator`) và toán hạng (`operand`)](#2.4)
* [2.5. Biểu thức (`expression`) và câu lệnh (`statement`)](#2.5)


* [II. Bài tập chương 2](#baitapchuong2)

* [III. Lời giải chương 2](#loigiaichuong2)


<a name="ghichepchuong2"></a>
### I. Các ghi chép trong chương 2
<a name="2.1">
#### 2.1. Giá trị và các kiểu của nó
- Giá trị (value) là một trong các điều cơ bản nhất đối với chương trình, chúng ta có thể bắt gặp các giá trị như `ký tự` hoặc `số`. 
- Ví dụ: `1,2` hoặc, `"hoc chu dong"`. Các giá trị ở ví dụ này sẽ có các kiểu (`type`) khác nhau: Như ví dụ trên thì `1` và `2` là có kiểu `interger` còn `hoc chu dong` có kiểu `string` (string là chuỗi các ký tự).
- Có thể gõ trực tiếp vào `interpreter` (màn hình CLI) trong python để thử, kết quả sẽ trả về kiểu (`type`) của giá trị (`value`). 
```python
>>> type(2)
<type 'int'>
>>> type ('hoc chu dong')
<type 'str'>
>>>
```
- Ngoài ra trong python còn có kểu giá trị gọi là `float` - kiểu động, ví dụ như 3.14 ; 6.96 ... Để minh chứng cho kiểu của các giá trị trên hay gõ vào CLI trong python như sau:
![float2](/images/float2.png)

hoặc

![float1](/images/float1.png)

- Nếu bạn gõ `type('3.2')` thì kiểu giá trị trả về sẽ là `string`, hãy thử:
```python
>>> type('3.2')
<type 'str'>
>>>
```

<a name="2.2"></a>
#### 2.2. Biến - `variables` trong python
- Biến là một khái niệm mạnh trong lập trình, ngôn ngữ lập trình dùng biến để tương tác và làm việc.
- Một biến được dùng để tham chiếu tới một giá trị nào đó.
- Dấu `=` trong trường hợp này được gọi là phép gán, tiếng Tây gọi là `assignment statement`
- Tưởng tượng biến như một cái hộp để đựng một vật gì đó. Lúc này hộp là biến còn vật là giá trị.
- Dưới là ví dụ về việc sử dụng biến và giá trị:
```python
a = 69 #Kieu interger
b = 9.6 #kieu float
chuoi = 'hoc chu dong' #Kieu string
```
- Ví dụ trên khai báo 03 biến với 03 giá trị có các kiểu khác nhau. 

<a name="2.3"></a>
#### 2.3. Tên của biến và các từ khóa trong python
##### Tên của biến 
- Biến cần được đặt theo quy tắc, nếu đặt sai chương trình sẽ gây lỗi.
- Cách đặt tên biến như sau:
```sh
- Không được bắt đầu bằng các ký tự đặc biệt.
- Không được trùng với từ khóa trong python. Danh sách từ khóa tham khảo ở dưới.
- Không được bắt đầu bằng một chữ số.
```
##### Từ khóa trong python (`keyword`)
- Từ khóa trong python được sử dụng để đặt tên cho các `lớp` - `class` trong python (khái niệm `lớp` sẽ được giải thích sau). Do vậy không được đặt tên biến trùng với lớp vì sẽ gây hiểu nhầm.
- Trong python 2.x có 31 từ khóa. Để xem danh sách các keyword trong python hãy thực hiện các lệnh dưới đây.
![keyword](/images/keyword.png)

<a name="2.4"></a>
#### 2.4. Toán tử (`operator`) và toán hạng (`operand`)
- Toán tử là các phép tính được biểu diễn bằng các ký tự đặc biệt, ví dụ:  
  + Phép cộng (addition):           `+`
  + Phép trừ (subtraction):         `-` 
  + Phép nhân (multiplication):     `*`
  + Phép chia (division):           `/`
  + Phép lũy thừa(exponentiation):  `**`
  + .... Ngoài ra còn rất nhiều phép toán khác trong thực tế, không tiện đề cập ở đây.
  
- Toán hạng là các giá trị được áp dụng trong phép tính.

<a name="2.5"></a>
#### 2.5. Biểu thức (`expression`) và câu lệnh (`statement`)

<a name="baitapchuong2"></a>
### II. Bài tập chương 2

<a name="loigiaichuong2></a>
### III. Lời giải chương 2