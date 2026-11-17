# 093 - Bài 93: Đếm cặp phần tử kề nhau trái dấu

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy đếm số lượng cặp phần tử kề nhau $(a_i, a_{i+1})$ ($0 \le i \le n - 2$) mà hai phần tử **trái dấu** nhau (tức là $a_i \cdot a_{i+1} < 0$).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số lượng cặp kề nhau trái dấu.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
1.0 -2.0 3.0 0.0 -4.0
```

Kết quả:

```text
2
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1.0 2.0 3.0 4.0
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
4
-1.0 2.0 -3.0 4.0
```

Kết quả:

```text
3
```

# Giải thích

- **Ví dụ 1:** Có $2$ cặp trái dấu: $(1.0, -2.0)$ và $(-2.0, 3.0)$. Số $0.0$ không mang dấu nên $(3.0, 0.0)$ và $(0.0, -4.0)$ không tính.
- **Ví dụ 2:** Các số đều dương nên kết quả là $0$.
- **Ví dụ 3:** Cả $3$ cặp liên tiếp đều đổi dấu.
