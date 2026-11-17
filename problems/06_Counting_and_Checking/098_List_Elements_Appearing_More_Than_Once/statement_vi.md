# 098 - Bài 98: Liệt kê giá trị xuất hiện quá 1 lần

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy liệt kê tất cả các giá trị xuất hiện **nhiều hơn $1$ lần** trong mảng. Mỗi giá trị thỏa mãn chỉ liệt kê đúng $1$ lần theo thứ tự xuất hiện đầu tiên.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra mỗi giá trị lặp lại đúng $1$ lần cách nhau bởi dấu cách, hoặc `EMPTY` nếu không có giá trị nào lặp lại.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6
4 2 4 7 2 4
```

Kết quả:

```text
4 2
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1 2 3 4
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
5
5 5 5 1 1
```

Kết quả:

```text
5 1
```

# Giải thích

- **Ví dụ 1:** $4$ xuất hiện $3$ lần và $2$ xuất hiện $2$ lần; $7$ chỉ xuất hiện $1$ lần.
- **Ví dụ 2:** Không có giá trị nào xuất hiện quá $1$ lần nên in `EMPTY`.
- **Ví dụ 3:** Cả $5$ và $1$ đều xuất hiện nhiều hơn $1$ lần.
