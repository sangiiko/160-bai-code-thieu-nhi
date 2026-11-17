# 091 - Bài 91: Đếm số lượng giá trị lớn nhất

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy đếm xem giá trị lớn nhất của mảng xuất hiện bao nhiêu lần.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số lần xuất hiện của giá trị lớn nhất.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
3.0 9.5 2.0 9.5 9.5
```

Kết quả:

```text
3
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-5.0 -1.0 -2.0 -8.0
```

Kết quả:

```text
1
```

# Ví dụ 3

Dữ liệu vào:

```text
3
4.0 4.0 4.0
```

Kết quả:

```text
3
```

# Giải thích

- **Ví dụ 1:** Giá trị lớn nhất là $9.5$, xuất hiện $3$ lần.
- **Ví dụ 2:** Giá trị lớn nhất là $-1.0$, xuất hiện $1$ lần.
- **Ví dụ 3:** Tất cả $3$ phần tử đều bằng giá trị lớn nhất $4.0$.
