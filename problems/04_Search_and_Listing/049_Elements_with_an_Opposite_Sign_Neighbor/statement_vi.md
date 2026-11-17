# 049 - Bài 49: Liệt kê giá trị có lân cận trái dấu

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy liệt kê tất cả các phần tử $a_i$ có ít nhất một phần tử lân cận ($a_{i-1}$ hoặc $a_{i+1}$) **trái dấu** với nó, tức là $a_i \cdot a_{i-1} < 0$ hoặc $a_i \cdot a_{i+1} < 0$.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các phần tử thỏa mãn theo thứ tự xuất hiện, cách nhau bởi dấu cách (sai số $\le 10^{-6}$), hoặc `EMPTY` nếu không có.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
1.5 2.0 -3.0 0.0 4.5
```

Kết quả:

```text
2.000000 -3.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1.0 2.0 3.0 4.0
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
4
-1.0 2.0 -3.0 4.0
```

Kết quả:

```text
-1.000000 2.000000 -3.000000 4.000000
```

# Giải thích

- **Ví dụ 1:** $2.0$ và $-3.0$ kề nhau và trái dấu. Số $0.0$ không mang dấu âm hay dương nên $0.0 \cdot 4.5 = 0 \not< 0$.
- **Ví dụ 2:** Mọi phần tử cùng dấu dương nên kết quả là `EMPTY`.
- **Ví dụ 3:** Mọi phần tử đều có lân cận trái dấu nên in ra toàn bộ mảng.
