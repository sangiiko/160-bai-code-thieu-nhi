# 096 - Bài 96: Liệt kê tần suất xuất hiện các giá trị

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy liệt kê mỗi giá trị phân biệt trong mảng cùng với số lần xuất hiện (tần suất) của nó. Mỗi giá trị chỉ liệt kê đúng $1$ lần theo **thứ tự xuất hiện đầu tiên**.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- Với mỗi giá trị phân biệt (theo thứ tự xuất hiện đầu tiên), in ra một dòng gồm `giá_trị tần_suất` cách nhau bởi một dấu cách.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6
5 2 5 3 2 5
```

Kết quả:

```text
5 3
2 2
3 1
```

# Ví dụ 2

Dữ liệu vào:

```text
4
7 7 7 7
```

Kết quả:

```text
7 4
```

# Ví dụ 3

Dữ liệu vào:

```text
3
-1 0 1
```

Kết quả:

```text
-1 1
0 1
1 1
```

# Giải thích

- **Ví dụ 1:** $5$ xuất hiện $3$ lần, $2$ xuất hiện $2$ lần, $3$ xuất hiện $1$ lần.
- **Ví dụ 2:** Chỉ có giá trị $7$ xuất hiện $4$ lần.
- **Ví dụ 3:** Ba giá trị phân biệt, mỗi giá trị xuất hiện $1$ lần.
