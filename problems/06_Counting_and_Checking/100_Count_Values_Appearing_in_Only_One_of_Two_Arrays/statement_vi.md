# 100 - Bài 100: Đếm giá trị chỉ xuất hiện ở 1 trong 2 mảng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho hai mảng số nguyên $a$ (gồm $n$ phần tử) và $b$ (gồm $m$ phần tử). Hãy đếm số lượng các **giá trị phân biệt** chỉ xuất hiện ở **đúng một trong hai mảng** (tức có mặt trong $a$ nhưng không có trong $b$, hoặc có mặt trong $b$ nhưng không có trong $a$).

# Dữ liệu vào

- Dòng đầu tiên chứa hai số nguyên dương $n$ và $m$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, \dots, a_{n-1}$.
- Dòng thứ ba chứa $m$ số nguyên $b_0, \dots, b_{m-1}$.

# Kết quả

- In ra số lượng giá trị phân biệt chỉ xuất hiện ở một trong hai mảng.

# Giới hạn

- $1 \le n, m \le 10^5$
- $-10^9 \le a_i, b_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
4 4
1 2 2 3
2 3 4 5
```

Kết quả:

```text
3
```

# Ví dụ 2

Dữ liệu vào:

```text
3 3
1 2 3
3 2 1
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
3 3
1 1 2
3 4 4
```

Kết quả:

```text
4
```

# Giải thích

- **Ví dụ 1:** Tập giá trị của $a$ là $\{1, 2, 3\}$, của $b$ là $\{2, 3, 4, 5\}$. Các giá trị chỉ có ở một mảng là $1, 4, 5$ (tổng cộng $3$).
- **Ví dụ 2:** Hai mảng chứa cùng tập giá trị $\{1, 2, 3\}$ nên kết quả là $0$.
- **Ví dụ 3:** Các giá trị chỉ có ở một mảng là $1, 2, 3, 4$ (có $4$ giá trị).
