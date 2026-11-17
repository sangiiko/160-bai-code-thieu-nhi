# 119 - Bài 119: Đếm phần tử lớn hơn mọi phần tử đứng trước

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy đếm số lượng phần tử $a_i$ ($0 \le i < n$) có giá trị **lớn hơn hẳn** tất cả các phần tử đứng đằng trước nó (tức $a_i > a_j$ với mọi $0 \le j < i$; riêng $a_0$ không có phần tử nào đứng trước nên luôn được tính).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số lượng phần tử thỏa mãn điều kiện.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
3 1 5 5 8
```

Kết quả:

```text
3
```

# Ví dụ 2

Dữ liệu vào:

```text
4
10 8 5 1
```

Kết quả:

```text
1
```

# Ví dụ 3

Dữ liệu vào:

```text
4
-5 -3 -4 0
```

Kết quả:

```text
3
```

# Giải thích

- **Ví dụ 1:** Các phần tử thỏa mãn là $a_0 = 3$, $a_2 = 5 > 3$, và $a_4 = 8 > 5$ ($a_3 = 5$ không lớn hơn hẳn $a_2 = 5$). Tổng là $3$.
- **Ví dụ 2:** Chỉ có phần tử đầu $a_0 = 10$ thỏa mãn ($1$).
- **Ví dụ 3:** Các phần tử thỏa mãn là $-5, -3, 0$ (tổng là $3$).
