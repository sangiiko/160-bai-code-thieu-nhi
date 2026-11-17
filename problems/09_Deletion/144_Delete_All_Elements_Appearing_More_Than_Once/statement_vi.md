# 144 - Bài 144: Xóa tất cả phần tử xuất hiện nhiều hơn 1 lần

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy xóa **tất cả** các phần tử thuộc về những giá trị có số lần xuất hiện lớn hơn $1$ trong mảng (tức chỉ giữ lại những phần tử xuất hiện đúng $1$ lần, theo thứ tự ban đầu).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các phần tử còn lại cách nhau bởi dấu cách, hoặc `EMPTY` nếu mọi phần tử đều bị xóa.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6
3 1 3 2 1 4
```

Kết quả:

```text
2 4
```

# Ví dụ 2

Dữ liệu vào:

```text
4
5 5 2 2
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
4
1 2 3 4
```

Kết quả:

```text
1 2 3 4
```

# Giải thích

- **Ví dụ 1:** $3$ và $1$ đều xuất hiện $2$ lần nên bị xóa hết; chỉ còn $2$ và $4$.
- **Ví dụ 2:** Mọi giá trị đều xuất hiện $2$ lần nên sau khi xóa còn `EMPTY`.
- **Ví dụ 3:** Mỗi giá trị xuất hiện đúng $1$ lần nên giữ nguyên toàn bộ mảng.
