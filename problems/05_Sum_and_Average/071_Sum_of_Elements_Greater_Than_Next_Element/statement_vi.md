# 071 - Bài 71: Tổng các giá trị lớn hơn trị tuyệt đối liền sau

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy tính tổng tất cả các phần tử $a_i$ ($0 \le i \le n - 2$) thỏa mãn lớn hơn hẳn trị tuyệt đối của phần tử đứng liền sau nó ($a_i > |a_{i+1}|$).

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
5.0 -3.0 4.0 -2.0 1.0
```

Kết quả:

```text
9.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-5.0 2.0 2.0 3.0
```

Kết quả:

```text
0.000000
```

# Ví dụ 3

Dữ liệu vào:

```text
1
10.0
```

Kết quả:

```text
0.000000
```

# Giải thích

- **Ví dụ 1:** $a_0 = 5.0 > |-3.0|$ và $a_2 = 4.0 > |-2.0|$. Tổng $= 5.0 + 4.0 = 9.0$.
- **Ví dụ 2:** $-5.0 < |2.0|$, $2.0 = |2.0|$, $2.0 < |3.0|$; tổng bằng $0$.
- **Ví dụ 3:** Mảng chỉ có 1 phần tử nên không có phần tử liền sau; tổng bằng $0$.
