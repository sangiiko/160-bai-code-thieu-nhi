# 129 - Bài 129: Trộn hai mảng tăng thành một mảng tăng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho hai mảng số thực $a$ (gồm $n$ phần tử) và $b$ (gồm $m$ phần tử) đều đã được sắp xếp theo thứ tự **tăng dần** (không giảm). Hãy trộn hai mảng này thành một mảng duy nhất gồm $n + m$ phần tử cũng được sắp xếp tăng dần (không giảm).

# Dữ liệu vào

- Dòng đầu tiên chứa hai số nguyên dương $n$ và $m$.
- Dòng thứ hai chứa $n$ số thực đã sắp xếp tăng dần.
- Dòng thứ ba chứa $m$ số thực đã sắp xếp tăng dần.

# Kết quả

- In ra $n + m$ số thực của mảng trộn theo thứ tự không giảm, cách nhau bởi dấu cách (sai số $\le 10^{-6}$).

# Giới hạn

- $1 \le n, m \le 10^5$
- $-10^9 \le a_i, b_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
3 4
1.0 4.0 7.0
2.0 3.0 5.0 8.0
```

Kết quả:

```text
1.000000 2.000000 3.000000 4.000000 5.000000 7.000000 8.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
2 2
-5.5 0.0
-3.2 4.1
```

Kết quả:

```text
-5.500000 -3.200000 0.000000 4.100000
```

# Ví dụ 3

Dữ liệu vào:

```text
1 3
10.0
1.0 2.0 3.0
```

Kết quả:

```text
1.000000 2.000000 3.000000 10.000000
```

# Giải thích

- **Ví dụ 1:** Trộn $[1, 4, 7]$ và $[2, 3, 5, 8]$ thu được $[1, 2, 3, 4, 5, 7, 8]$.
- **Ví dụ 2:** Trộn các số âm và dương thu được $[-5.5, -3.2, 0.0, 4.1]$.
- **Ví dụ 3:** Trộn $[10.0]$ và $[1.0, 2.0, 3.0]$ thu được $[1.0, 2.0, 3.0, 10.0]$.
