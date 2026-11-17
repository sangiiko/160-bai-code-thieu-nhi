# 044 - Bài 44: Liệt kê các số thực thuộc đoạn [x, y]

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$ và hai số thực $x, y$ ($x \le y$). Hãy liệt kê tất cả các phần tử $a_i$ thuộc đoạn $[x, y]$ (tức $x \le a_i \le y$) theo đúng thứ tự xuất hiện.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$ và hai số thực $x, y$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các phần tử thuộc đoạn $[x, y]$ cách nhau bởi dấu cách (sai số $\le 10^{-6}$), hoặc `EMPTY` nếu không có phần tử nào.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le x \le y \le 10^9$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5 1.0 5.0
0.5 1.0 3.2 5.5 4.8
```

Kết quả:

```text
1.000000 3.200000 4.800000
```

# Ví dụ 2

Dữ liệu vào:

```text
4 10.0 20.0
-1.0 0.0 9.99 20.01
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
4 -2.5 2.5
-2.5 0.0 2.5 3.0
```

Kết quả:

```text
-2.500000 0.000000 2.500000
```

# Giải thích

- **Ví dụ 1:** Trong $[1.0, 5.0]$ có các phần tử $1.0, 3.2, 4.8$.
- **Ví dụ 2:** Không có phần tử nào nằm trong $[10.0, 20.0]$ nên in `EMPTY`.
- **Ví dụ 3:** Hai đầu mút $-2.5$ và $2.5$ đều thuộc đoạn đóng $[-2.5, 2.5]$.
