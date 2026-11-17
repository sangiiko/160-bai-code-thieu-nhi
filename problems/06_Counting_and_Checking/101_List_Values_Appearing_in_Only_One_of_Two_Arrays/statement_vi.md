# 101 - Bài 101: Liệt kê giá trị chỉ xuất hiện ở 1 trong 2 mảng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho hai mảng số nguyên $a$ (gồm $n$ phần tử) và $b$ (gồm $m$ phần tử). Hãy liệt kê tất cả các **giá trị phân biệt** chỉ xuất hiện ở **đúng một trong hai mảng** (trước hết liệt kê các giá trị chỉ có trong $a$ theo thứ tự xuất hiện đầu tiên, sau đó đến các giá trị chỉ có trong $b$ theo thứ tự xuất hiện đầu tiên).

# Dữ liệu vào

- Dòng đầu tiên chứa hai số nguyên dương $n$ và $m$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, \dots, a_{n-1}$.
- Dòng thứ ba chứa $m$ số nguyên $b_0, \dots, b_{m-1}$.

# Kết quả

- In ra các giá trị thỏa mãn cách nhau bởi dấu cách, hoặc `EMPTY` nếu không có giá trị nào.

# Giới hạn

- $1 \le n, m \le 10^5$
- $-10^9 \le a_i, b_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
4 4
1 2 2 3
2 3 4 5
```

Kết quả:

```text
1 4 5
```

# Ví dụ 2

Dữ liệu vào:

```text
3 3
1 2 3
1 2 3
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
3 2
7 7 8
8 9
```

Kết quả:

```text
7 9
```

# Giải thích

- **Ví dụ 1:** $1$ chỉ có ở $a$; $4$ và $5$ chỉ có ở $b$.
- **Ví dụ 2:** Mọi giá trị đều xuất hiện ở cả hai mảng nên in `EMPTY`.
- **Ví dụ 3:** $7$ chỉ có ở $a$ và $9$ chỉ có ở $b$ (mỗi giá trị in $1$ lần).
