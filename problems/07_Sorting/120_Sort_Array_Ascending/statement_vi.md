# 120 - Bài 120: Sắp xếp mảng tăng dần

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy sắp xếp các phần tử của mảng theo thứ tự **tăng dần** (không giảm: $a_0 \le a_1 \le \dots \le a_{n-1}$).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra $n$ số thực sau khi sắp xếp tăng dần, cách nhau bởi dấu cách (sai số $\le 10^{-6}$).

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
3.5 -1.0 2.0 0.0 2.0
```

Kết quả:

```text
-1.000000 0.000000 2.000000 2.000000 3.500000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
10.0 5.0 -2.0 -10.0
```

Kết quả:

```text
-10.000000 -2.000000 5.000000 10.000000
```

# Ví dụ 3

Dữ liệu vào:

```text
1
4.25
```

Kết quả:

```text
4.250000
```

# Giải thích

- **Ví dụ 1:** Sau khi sắp xếp không giảm: $-1.0, 0.0, 2.0, 2.0, 3.5$.
- **Ví dụ 2:** Mảng ban đầu giảm dần được đảo thành tăng dần.
- **Ví dụ 3:** Mảng 1 phần tử giữ nguyên.
