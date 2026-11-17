# 077 - Bài 77: Trung bình cộng các số nguyên tố

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tính trung bình cộng của tất cả các **số nguyên tố** có trong mảng. Nếu mảng không có số nguyên tố nào, in ra `0`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra trung bình cộng các số nguyên tố (sai số $\le 10^{-6}$), hoặc `0` nếu không có số nguyên tố.

# Giới hạn

- $1 \le n \le 10^4$
- $-10^6 \le a_i \le 10^6$

# Ví dụ 1

Dữ liệu vào:

```text
5
2 4 5 9 11
```

Kết quả:

```text
6.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1 4 6 9
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
4
2 3 5 7
```

Kết quả:

```text
4.250000
```

# Giải thích

- **Ví dụ 1:** Các số nguyên tố là $2, 5, 11$. Trung bình cộng $= (2 + 5 + 11) / 3 = 6.0$.
- **Ví dụ 2:** Không có số nguyên tố nào nên in `0`.
- **Ví dụ 3:** Trung bình cộng $= (2 + 3 + 5 + 7) / 4 = 4.25$.
