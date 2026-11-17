# 095 - Bài 95: Đếm số lượng giá trị phân biệt

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy đếm xem trong mảng có bao nhiêu giá trị **phân biệt** (khác nhau).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số lượng giá trị phân biệt trong mảng.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6
1 2 2 3 1 4
```

Kết quả:

```text
4
```

# Ví dụ 2

Dữ liệu vào:

```text
5
7 7 7 7 7
```

Kết quả:

```text
1
```

# Ví dụ 3

Dữ liệu vào:

```text
4
-5 5 0 -5
```

Kết quả:

```text
3
```

# Giải thích

- **Ví dụ 1:** Các giá trị khác nhau là $1, 2, 3, 4$ (có $4$ giá trị).
- **Ví dụ 2:** Tất cả phần tử đều bằng $7$ nên chỉ có $1$ giá trị phân biệt.
- **Ví dụ 3:** Các giá trị phân biệt là $-5, 5, 0$ (có $3$ giá trị).
