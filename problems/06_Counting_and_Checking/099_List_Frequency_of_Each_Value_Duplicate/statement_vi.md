# 099 - Bài 99: Liệt kê tần suất xuất hiện (2)

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy liệt kê tần suất xuất hiện của từng giá trị trong mảng, mỗi giá trị phân biệt chỉ liệt kê $1$ lần theo thứ tự xuất hiện đầu tiên.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- Với mỗi giá trị phân biệt, in ra `giá_trị số_lần` trên một dòng riêng.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
10 20 10 30 20
```

Kết quả:

```text
10 2
20 2
30 1
```

# Ví dụ 2

Dữ liệu vào:

```text
3
0 0 0
```

Kết quả:

```text
0 3
```

# Ví dụ 3

Dữ liệu vào:

```text
4
1 2 3 4
```

Kết quả:

```text
1 1
2 1
3 1
4 1
```

# Giải thích

- **Ví dụ 1:** $10$ xuất hiện $2$ lần, $20$ xuất hiện $2$ lần, $30$ xuất hiện $1$ lần.
- **Ví dụ 2:** $0$ xuất hiện $3$ lần.
- **Ví dụ 3:** Mỗi giá trị xuất hiện $1$ lần.
