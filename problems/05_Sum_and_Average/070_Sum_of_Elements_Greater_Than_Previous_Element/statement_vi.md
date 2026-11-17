# 070 - Bài 70: Tổng các giá trị lớn hơn phần tử liền trước

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy tính tổng tất cả các phần tử $a_i$ ($1 \le i \le n - 1$) lớn hơn hẳn phần tử đứng liền trước nó ($a_i > a_{i-1}$).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra tổng cần tìm (sai số $\le 10^{-6}$).

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
2.0 5.0 3.0 4.5 4.5
```

Kết quả:

```text
9.500000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
10.0 8.0 5.0 1.0
```

Kết quả:

```text
0.000000
```

# Ví dụ 3

Dữ liệu vào:

```text
4
1.0 2.0 3.0 4.0
```

Kết quả:

```text
9.000000
```

# Giải thích

- **Ví dụ 1:** $a_1 = 5.0 > a_0 = 2.0$ và $a_3 = 4.5 > a_2 = 3.0$ ($a_4 = 4.5$ bằng $a_3$ nên không tính). Tổng $= 9.5$.
- **Ví dụ 2:** Mảng giảm dần nên không phần tử nào thỏa mãn; tổng bằng $0$.
- **Ví dụ 3:** Các phần tử $2.0, 3.0, 4.0$ đều lớn hơn phần tử liền trước; tổng $= 9.0$.
