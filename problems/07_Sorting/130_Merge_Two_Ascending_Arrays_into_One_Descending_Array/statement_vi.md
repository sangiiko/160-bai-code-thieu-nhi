# 130 - Bài 130: Trộn hai mảng tăng thành một mảng giảm

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho hai mảng số thực $a$ (gồm $n$ phần tử) và $b$ (gồm $m$ phần tử) đều đã được sắp xếp theo thứ tự **tăng dần** (không giảm). Hãy trộn hai mảng này thành một mảng duy nhất gồm $n + m$ phần tử được sắp xếp theo thứ tự **giảm dần** (không tăng).

# Dữ liệu vào

- Dòng đầu tiên chứa hai số nguyên dương $n$ và $m$.
- Dòng thứ hai chứa $n$ số thực đã sắp xếp tăng dần.
- Dòng thứ ba chứa $m$ số thực đã sắp xếp tăng dần.

# Kết quả

- In ra $n + m$ số thực của mảng trộn theo thứ tự không tăng, cách nhau bởi dấu cách (sai số $\le 10^{-6}$).

# Giới hạn

- $1 \le n, m \le 10^5$
- $-10^9 \le a_i, b_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
3 3
1.0 4.0 7.0
2.0 5.0 8.0
```

Kết quả:

```text
8.000000 7.000000 5.000000 4.000000 2.000000 1.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
2 2
-10.0 0.0
-5.0 5.0
```

Kết quả:

```text
5.000000 0.000000 -5.000000 -10.000000
```

# Ví dụ 3

Dữ liệu vào:

```text
3 1
1.0 2.0 3.0
2.0
```

Kết quả:

```text
3.000000 2.000000 2.000000 1.000000
```

# Giải thích

- **Ví dụ 1:** Trộn hai mảng tăng theo chiều từ lớn đến nhỏ thu được $[8, 7, 5, 4, 2, 1]$.
- **Ví dụ 2:** Kết quả giảm dần là $[5.0, 0.0, -5.0, -10.0]$.
- **Ví dụ 3:** Giá trị $2.0$ xuất hiện ở cả hai mảng đều được giữ lại: $[3.0, 2.0, 2.0, 1.0]$.
