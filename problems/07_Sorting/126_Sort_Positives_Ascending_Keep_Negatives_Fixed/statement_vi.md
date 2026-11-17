# 126 - Bài 126: Sắp xếp số dương tăng dần, số âm giữ nguyên vị trí

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy sắp xếp các phần tử **dương** ($a_i > 0$) theo thứ tự tăng dần trên các vị trí ban đầu của chúng, trong khi các phần tử âm (và số $0$, tức $a_i \le 0$) giữ nguyên vị trí.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra mảng kết quả gồm $n$ số thực cách nhau bởi dấu cách (sai số $\le 10^{-6}$).

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6
5.0 -2.0 1.5 0.0 3.0 -4.0
```

Kết quả:

```text
1.500000 -2.000000 3.000000 0.000000 5.000000 -4.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-3.0 -1.0 -2.0 0.0
```

Kết quả:

```text
-3.000000 -1.000000 -2.000000 0.000000
```

# Ví dụ 3

Dữ liệu vào:

```text
4
9.0 4.0 7.0 1.0
```

Kết quả:

```text
1.000000 4.000000 7.000000 9.000000
```

# Giải thích

- **Ví dụ 1:** Các số dương $[5.0, 1.5, 3.0]$ tại chỉ số $0, 2, 4$ được sắp thành $[1.5, 3.0, 5.0]$; các số $-2.0, 0.0, -4.0$ giữ nguyên.
- **Ví dụ 2:** Không có số dương nào nên mảng giữ nguyên.
- **Ví dụ 3:** Toàn bộ mảng là số dương nên được sắp xếp tăng dần.
