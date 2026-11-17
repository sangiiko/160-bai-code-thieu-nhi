# 041 - Bài 41: Liệt kê các cặp (a, b) thỏa a <= b

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng một chiều gồm $n$ số thực **đôi một phân biệt** ($n > 2$). Hãy liệt kê tất cả các cặp phần tử $(a, b)$ lấy từ hai vị trí khác nhau trong mảng thỏa mãn $a \le b$ (tức $a < b$ vì các phần tử phân biệt).

Các cặp được in theo thứ tự tăng dần của $a$, nếu cùng $a$ thì tăng dần của $b$.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên $n$.
- Dòng thứ hai chứa $n$ số thực đôi một phân biệt.

# Kết quả

- In ra $\frac{n(n-1)}{2}$ dòng, mỗi dòng gồm hai số thực $a$ và $b$ cách nhau bởi dấu cách.

# Giới hạn

- $3 \le n \le 1000$
- $-10^9 \le a_i \le 10^9$, các phần tử đôi một khác nhau.

# Ví dụ 1

Dữ liệu vào:

```text
3
3.0 1.0 2.0
```

Kết quả:

```text
1.000000 2.000000
1.000000 3.000000
2.000000 3.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-1.5 2.0 0.5 1.0
```

Kết quả:

```text
-1.500000 0.500000
-1.500000 1.000000
-1.500000 2.000000
0.500000 1.000000
0.500000 2.000000
1.000000 2.000000
```

# Ví dụ 3

Dữ liệu vào:

```text
3
10.0 5.0 1.0
```

Kết quả:

```text
1.000000 5.000000
1.000000 10.000000
5.000000 10.000000
```

# Giải thích

- **Ví dụ 1:** Từ $\{1.0, 2.0, 3.0\}$ có $3$ cặp thỏa $a < b$: $(1.0, 2.0)$, $(1.0, 3.0)$ và $(2.0, 3.0)$.
- **Ví dụ 2:** Từ $\{-1.5, 0.5, 1.0, 2.0\}$ liệt kê đủ $6$ cặp theo thứ tự từ điển tăng dần.
- **Ví dụ 3:** Liệt kê $3$ cặp từ $\{1.0, 5.0, 10.0\}$.
