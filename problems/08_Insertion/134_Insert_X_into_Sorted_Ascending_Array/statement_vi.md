# 134 - Bài 134: Thêm x vào mảng tăng giữ nguyên tính tăng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực đã được sắp xếp theo thứ tự **tăng dần** (không giảm) và một số thực $x$. Hãy chèn $x$ vào mảng sao cho mảng mới gồm $n + 1$ phần tử vẫn giữ nguyên tính tăng dần (không giảm).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$ và số thực $x$.
- Dòng thứ hai chứa $n$ số thực đã sắp xếp không giảm.

# Kết quả

- In ra mảng kết quả gồm $n + 1$ số thực cách nhau bởi dấu cách (sai số $\le 10^{-6}$).

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le x, a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5 4.5
1.0 2.0 4.0 6.0 8.0
```

Kết quả:

```text
1.000000 2.000000 4.000000 4.500000 6.000000 8.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
3 -10.0
-5.0 0.0 5.0
```

Kết quả:

```text
-10.000000 -5.000000 0.000000 5.000000
```

# Ví dụ 3

Dữ liệu vào:

```text
3 10.0
-5.0 0.0 5.0
```

Kết quả:

```text
-5.000000 0.000000 5.000000 10.000000
```

# Giải thích

- **Ví dụ 1:** $4.5$ được chèn vào giữa $4.0$ và $6.0$.
- **Ví dụ 2:** $-10.0$ nhỏ hơn mọi phần tử nên được chèn vào đầu mảng.
- **Ví dụ 3:** $10.0$ lớn hơn mọi phần tử nên được chèn vào cuối mảng.
