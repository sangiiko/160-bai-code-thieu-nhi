# 121 - Bài 121: Sắp xếp mảng giảm dần

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy sắp xếp các phần tử của mảng theo thứ tự **giảm dần** (không tăng: $a_0 \ge a_1 \ge \dots \ge a_{n-1}$).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra $n$ số thực sau khi sắp xếp giảm dần, cách nhau bởi dấu cách (sai số $\le 10^{-6}$).

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
3.500000 2.000000 2.000000 0.000000 -1.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-5.0 -1.0 0.0 10.0
```

Kết quả:

```text
10.000000 0.000000 -1.000000 -5.000000
```

# Ví dụ 3

Dữ liệu vào:

```text
3
2.5 2.5 2.5
```

Kết quả:

```text
2.500000 2.500000 2.500000
```

# Giải thích

- **Ví dụ 1:** Sau khi sắp xếp không tăng: $3.5, 2.0, 2.0, 0.0, -1.0$.
- **Ví dụ 2:** Mảng ban đầu tăng dần được sắp xếp lại giảm dần.
- **Ví dụ 3:** Mọi phần tử bằng nhau nên thứ tự không đổi.
