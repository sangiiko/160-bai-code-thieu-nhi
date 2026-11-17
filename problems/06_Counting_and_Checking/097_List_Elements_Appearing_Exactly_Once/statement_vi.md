# 097 - Bài 97: Liệt kê giá trị xuất hiện đúng 1 lần

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy liệt kê tất cả các phần tử xuất hiện **đúng $1$ lần** trong mảng theo đúng thứ tự xuất hiện.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các giá trị xuất hiện đúng $1$ lần cách nhau bởi dấu cách, hoặc `EMPTY` nếu không có phần tử nào.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6
4 2 4 7 2 9
```

Kết quả:

```text
7 9
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1 2 1 2
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
3
10 20 30
```

Kết quả:

```text
10 20 30
```

# Giải thích

- **Ví dụ 1:** $4$ và $2$ xuất hiện $2$ lần; chỉ có $7$ và $9$ xuất hiện đúng $1$ lần.
- **Ví dụ 2:** Mọi phần tử đều lặp lại nên in ra `EMPTY`.
- **Ví dụ 3:** Cả ba phần tử đều xuất hiện đúng $1$ lần.
