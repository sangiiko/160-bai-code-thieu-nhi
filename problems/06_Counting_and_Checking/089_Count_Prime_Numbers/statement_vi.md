# 089 - Bài 89: Đếm số nguyên tố

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy đếm số lượng **số nguyên tố** có trong mảng.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số lượng số nguyên tố trong mảng.

# Giới hạn

- $1 \le n \le 10^4$
- $-10^6 \le a_i \le 10^6$

# Ví dụ 1

Dữ liệu vào:

```text
6
2 3 4 5 9 11
```

Kết quả:

```text
4
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-2 0 1 4
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
3
2 2 2
```

Kết quả:

```text
3
```

# Giải thích

- **Ví dụ 1:** Các số nguyên tố là $2, 3, 5, 11$ (có $4$ số).
- **Ví dụ 2:** Không có số nguyên tố nào nên kết quả là $0$.
- **Ví dụ 3:** Giá trị $2$ xuất hiện $3$ lần, đếm cả $3$ lần.
