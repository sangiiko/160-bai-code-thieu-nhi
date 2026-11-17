# 128 - Bài 128: Sắp xếp dương tăng, âm giảm giữ vị trí tương đối

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy sắp xếp các số **dương** ($a_i > 0$) tăng dần trên các vị trí dương, và sắp xếp các số **âm** ($a_i < 0$) giảm dần trên các vị trí âm (các phần tử $0$ nếu có sẽ giữ nguyên vị trí).

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
5.0 -8.0 2.0 -1.0 3.0 -4.0
```

Kết quả:

```text
2.000000 -1.000000 3.000000 -4.000000 5.000000 -8.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
5
4.0 0.0 -5.0 1.0 -2.0
```

Kết quả:

```text
1.000000 0.000000 -2.000000 4.000000 -5.000000
```

# Ví dụ 3

Dữ liệu vào:

```text
3
-3.0 -1.0 -2.0
```

Kết quả:

```text
-1.000000 -2.000000 -3.000000
```

# Giải thích

- **Ví dụ 1:** Số dương $[5.0, 2.0, 3.0] \to [2.0, 3.0, 5.0]$; số âm $[-8.0, -1.0, -4.0] \to [-1.0, -4.0, -8.0]$.
- **Ví dụ 2:** Số $0.0$ giữ nguyên ở chỉ số $1$; số dương thành $[1.0, 4.0]$; số âm giảm dần thành $[-2.0, -5.0]$.
- **Ví dụ 3:** Chỉ có số âm nên được sắp giảm dần thành $[-1.0, -2.0, -3.0]$.
