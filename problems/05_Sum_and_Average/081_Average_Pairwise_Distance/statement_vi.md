# 081 - Bài 81: Khoảng cách trung bình giữa các phần tử

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$ ($n \ge 2$). Hãy tính khoảng cách trung bình giữa mọi cặp phần tử ở hai vị trí khác nhau $(i, j)$ ($0 \le i < j < n$) trong mảng:
$$\frac{2}{n(n-1)} \sum_{0 \le i < j < n} |a_i - a_j|$$

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra khoảng cách trung bình cần tìm (sai số $\le 10^{-6}$).

# Giới hạn

- $2 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
3
1.0 3.0 7.0
```

Kết quả:

```text
4.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
5.0 5.0 5.0 5.0
```

Kết quả:

```text
0.000000
```

# Ví dụ 3

Dữ liệu vào:

```text
2
-2.5 7.5
```

Kết quả:

```text
10.000000
```

# Giải thích

- **Ví dụ 1:** Các khoảng cách cặp: $|1-3|=2$, $|1-7|=6$, $|3-7|=4$. Trung bình $= (2 + 6 + 4) / 3 = 4.0$.
- **Ví dụ 2:** Mọi phần tử bằng nhau nên khoảng cách trung bình bằng $0$.
- **Ví dụ 3:** Chỉ có 1 cặp với khoảng cách $|-2.5 - 7.5| = 10.0$.
