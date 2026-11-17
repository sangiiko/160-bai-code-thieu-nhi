# 104 - Bài 104: Đếm số lượng số nguyên tố phân biệt

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy đếm số lượng các **số nguyên tố phân biệt** (mỗi giá trị nguyên tố chỉ tính $1$ lần dù xuất hiện nhiều lần) có trong mảng.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số lượng số nguyên tố phân biệt trong mảng.

# Giới hạn

- $1 \le n \le 10^4$
- $-10^6 \le a_i \le 10^6$

# Ví dụ 1

Dữ liệu vào:

```text
6
2 3 2 5 3 4
```

Kết quả:

```text
3
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
7 7 7 7
```

Kết quả:

```text
1
```

# Giải thích

- **Ví dụ 1:** Các số nguyên tố phân biệt là $2, 3, 5$ (có $3$ số).
- **Ví dụ 2:** Không có số nguyên tố nào nên kết quả là $0$.
- **Ví dụ 3:** Chỉ có $1$ số nguyên tố phân biệt là $7$.
