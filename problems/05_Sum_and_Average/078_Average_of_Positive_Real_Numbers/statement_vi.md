# 078 - Bài 78: Trung bình cộng các số dương

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy tính trung bình cộng của tất cả các giá trị **dương** ($a_i > 0$) có trong mảng. Nếu không có giá trị dương nào, in ra `0`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra trung bình cộng các giá trị dương (sai số $\le 10^{-6}$).

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
-2.0 3.0 0.0 6.0 9.0
```

Kết quả:

```text
6.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
3
-1.0 0.0 -5.0
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
3
1.5 2.5 5.0
```

Kết quả:

```text
3.000000
```

# Giải thích

- **Ví dụ 1:** Các số dương là $3.0, 6.0, 9.0$; trung bình $= 18.0 / 3 = 6.0$.
- **Ví dụ 2:** Không có số dương nào nên kết quả bằng $0$.
- **Ví dụ 3:** Trung bình cộng $= (1.5 + 2.5 + 5.0) / 3 = 3.0$.
