# 067 - Bài 67: Tổng các giá trị dương trong mảng số thực

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy tính tổng tất cả các giá trị **dương** ($a_i > 0$) có trong mảng. Nếu không có giá trị dương nào, kết quả là `0`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra tổng các giá trị dương (sai số $\le 10^{-6}$).

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
-2.0 3.5 0.0 1.5 -4.0
```

Kết quả:

```text
5.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
3
-5.0 0.0 -1.2
```

Kết quả:

```text
0.000000
```

# Ví dụ 3

Dữ liệu vào:

```text
3
1.25 2.75 4.0
```

Kết quả:

```text
8.000000
```

# Giải thích

- **Ví dụ 1:** Các số dương là $3.5$ và $1.5$, tổng bằng $5.0$.
- **Ví dụ 2:** Không có giá trị dương nào nên tổng bằng $0$.
- **Ví dụ 3:** Tất cả đều dương, tổng bằng $8.0$.
