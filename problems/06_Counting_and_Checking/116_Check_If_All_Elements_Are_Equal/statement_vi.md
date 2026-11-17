# 116 - Bài 116: Kiểm tra các phần tử bằng nhau

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy kiểm tra xem tất cả các phần tử trong mảng có **bằng nhau** hay không.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra `1` nếu mọi phần tử đều bằng nhau, ngược lại in ra `0`.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
4
7 7 7 7
```

Kết quả:

```text
1
```

# Ví dụ 2

Dữ liệu vào:

```text
4
7 7 8 7
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
1
-100
```

Kết quả:

```text
1
```

# Giải thích

- **Ví dụ 1:** Tất cả phần tử đều bằng $7$ (`1`).
- **Ví dụ 2:** Có phần tử $8 \ne 7$ (`0`).
- **Ví dụ 3:** Mảng có $1$ phần tử nên mọi phần tử đều bằng nhau (`1`).
