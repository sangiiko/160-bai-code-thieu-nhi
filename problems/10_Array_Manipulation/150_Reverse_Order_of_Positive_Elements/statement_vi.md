# 150 - Bài 150: Đảo ngược thứ tự các số dương

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy đảo ngược thứ tự của riêng các số **dương** ($a_i > 0$) trên các vị trí ban đầu của chúng, trong khi các phần tử không dương ($a_i \le 0$) giữ nguyên vị trí.

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
5
1.5 -2.0 3.0 0.0 8.5
```

Kết quả:

```text
8.500000 -2.000000 3.000000 0.000000 1.500000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-1.0 0.0 -3.0 -5.0
```

Kết quả:

```text
-1.000000 0.000000 -3.000000 -5.000000
```

# Ví dụ 3

Dữ liệu vào:

```text
3
2.0 4.0 6.0
```

Kết quả:

```text
6.000000 4.000000 2.000000
```

# Giải thích

- **Ví dụ 1:** Các số dương $[1.5, 3.0, 8.5]$ đảo thành $[8.5, 3.0, 1.5]$; $-2.0$ và $0.0$ giữ nguyên.
- **Ví dụ 2:** Không có số dương nào nên mảng giữ nguyên.
- **Ví dụ 3:** Toàn bộ là số dương nên đảo ngược cả mảng.
