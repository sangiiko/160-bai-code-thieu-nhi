# 058 - Bài 58: Liệt kê các giá trị cực đại

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$ ($n \ge 2$). Một phần tử $a_i$ được gọi là **cực đại** nếu nó lớn hơn hẳn tất cả các phần tử lân cận của nó (lớn hơn $a_{i-1}$ nếu $i > 0$, và lớn hơn $a_{i+1}$ nếu $i < n - 1$). Hãy liệt kê tất cả các giá trị cực đại theo thứ tự xuất hiện.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các phần tử cực đại cách nhau bởi dấu cách (sai số $\le 10^{-6}$), hoặc `EMPTY` nếu không tồn tại.

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
5.000000 8.000000 4.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
3.0 3.0 3.0 3.0
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
4
1.0 2.0 3.0 4.0
```

Kết quả:

```text
4.000000
```

# Giải thích

- **Ví dụ 1:** $5.0 > 2.0$; $8.0 > 2.0$ và $8.0 > 3.0$; $4.0 > 3.0$.
- **Ví dụ 2:** Mọi phần tử bằng nhau nên không có phần tử nào lớn hơn hẳn lân cận; in `EMPTY`.
- **Ví dụ 3:** Mảng tăng dần nên chỉ có phần tử cuối $4.0 > 3.0$ là cực đại.
