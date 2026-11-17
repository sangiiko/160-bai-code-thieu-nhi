# 072 - Bài 72: Tổng các phần tử cực đại

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$ ($n \ge 2$). Một phần tử $a_i$ được gọi là **cực đại** nếu nó lớn hơn hẳn các phần tử xung quanh (lớn hơn $a_{i-1}$ nếu $i > 0$, và lớn hơn $a_{i+1}$ nếu $i < n - 1$; mỗi phần tử có tối đa $2$ phần tử xung quanh). Hãy tính tổng các phần tử cực đại.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra tổng các phần tử cực đại (sai số $\le 10^{-6}$).

# Giới hạn

- $2 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
5.0 2.0 8.0 3.0 4.0
```

Kết quả:

```text
17.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
3.0 3.0 3.0 3.0
```

Kết quả:

```text
0.000000
```

# Ví dụ 3

Dữ liệu vào:

```text
4
1.0 5.0 2.0 6.0
```

Kết quả:

```text
11.000000
```

# Giải thích

- **Ví dụ 1:** Các phần tử cực đại là $5.0, 8.0, 4.0$; tổng $= 17.0$.
- **Ví dụ 2:** Không có phần tử nào lớn hơn hẳn phần tử xung quanh; tổng $= 0$.
- **Ví dụ 3:** Các phần tử cực đại là $5.0$ và $6.0$; tổng $= 11.0$.
