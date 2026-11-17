# 074 - Bài 74: Tổng các số chính phương

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tính tổng tất cả các **số chính phương** ($a_i = k^2$ với $k \ge 0$ nguyên) trong mảng.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra tổng các số chính phương dưới dạng số nguyên 64-bit.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
1 3 4 9 -16
```

Kết quả:

```text
14
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-4 2 3 7
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
4
0 25 100 10
```

Kết quả:

```text
125
```

# Giải thích

- **Ví dụ 1:** Các số chính phương là $1, 4, 9$ ($-16 < 0$ không phải); tổng $= 14$.
- **Ví dụ 2:** Không có số chính phương nào nên tổng bằng $0$.
- **Ví dụ 3:** Các số chính phương là $0, 25, 100$; tổng $= 125$.
