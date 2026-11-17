# 050 - Bài 50: Liệt kê vị trí có giá trị lớn nhất

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$ (đánh số từ $0$ đến $n - 1$). Hãy liệt kê tất cả các vị trí (chỉ số) mà giá trị tại đó bằng giá trị lớn nhất của mảng.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra tất cả các chỉ số (tính từ $0$) theo thứ tự tăng dần, cách nhau bởi dấu cách.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
3.5 9.0 2.1 9.0 4.0
```

Kết quả:

```text
1 3
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-5.0 -2.0 -2.0 -8.0
```

Kết quả:

```text
1 2
```

# Ví dụ 3

Dữ liệu vào:

```text
3
7.0 7.0 7.0
```

Kết quả:

```text
0 1 2
```

# Giải thích

- **Ví dụ 1:** Giá trị lớn nhất là $9.0$, xuất hiện tại các chỉ số $1$ và $3$.
- **Ví dụ 2:** Giá trị lớn nhất là $-2.0$ tại các chỉ số $1$ và $2$.
- **Ví dụ 3:** Tất cả phần tử đều đạt giá trị lớn nhất nên in ra $0, 1, 2$.
