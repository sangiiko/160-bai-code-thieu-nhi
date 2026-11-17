# 103 - Bài 103: Liệt kê giá trị xuất hiện nhiều nhất

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy liệt kê tất cả các giá trị có **số lần xuất hiện nhiều nhất** trong mảng (mỗi giá trị in $1$ lần theo thứ tự xuất hiện đầu tiên).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các giá trị xuất hiện nhiều nhất cách nhau bởi dấu cách.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6
1 2 1 3 2 4
```

Kết quả:

```text
1 2
```

# Ví dụ 2

Dữ liệu vào:

```text
5
5 3 5 2 5
```

Kết quả:

```text
5
```

# Ví dụ 3

Dữ liệu vào:

```text
3
7 8 9
```

Kết quả:

```text
7 8 9
```

# Giải thích

- **Ví dụ 1:** Số lần xuất hiện nhiều nhất là $2$, đạt được bởi các giá trị $1$ và $2$.
- **Ví dụ 2:** Giá trị $5$ xuất hiện $3$ lần (nhiều nhất).
- **Ví dụ 3:** Cả ba giá trị đều xuất hiện $1$ lần (bằng nhau).
