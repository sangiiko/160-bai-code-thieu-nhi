# 132 - Bài 132: Nhập mảng sắp xếp giảm dần

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho lần lượt $n$ số nguyên được nhập vào theo thứ tự $a_0, a_1, \dots, a_{n-1}$. Hãy xây dựng mảng sao cho ngay trong quá trình nhập (mỗi khi nhận thêm một số mới, chèn nó vào đúng vị trí thích hợp), mảng luôn duy trì thứ tự **giảm dần** (không tăng). Hãy in ra mảng sau khi đã nhập xong cả $n$ phần tử.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$ theo thứ tự nhập.

# Kết quả

- In ra mảng giảm dần gồm $n$ số nguyên cách nhau bởi dấu cách.

# Giới hạn

- $1 \le n \le 10^4$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
3 1 4 2 5
```

Kết quả:

```text
5 4 3 2 1
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-10 0 -5 10
```

Kết quả:

```text
10 0 -5 -10
```

# Ví dụ 3

Dữ liệu vào:

```text
1
42
```

Kết quả:

```text
42
```

# Giải thích

- **Ví dụ 1:** Quá trình chèn: $[3] \to [3, 1] \to [4, 3, 1] \to [4, 3, 2, 1] \to [5, 4, 3, 2, 1]$.
- **Ví dụ 2:** Mảng cuối cùng thu được theo thứ tự không tăng là $[10, 0, -5, -10]$.
- **Ví dụ 3:** Mảng chỉ có 1 phần tử $42$.
