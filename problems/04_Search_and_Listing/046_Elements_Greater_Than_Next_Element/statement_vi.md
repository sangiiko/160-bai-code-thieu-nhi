# 046 - Bài 46: Liệt kê giá trị lớn hơn trị tuyệt đối liền sau

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy liệt kê tất cả các phần tử $a_i$ ($0 \le i \le n - 2$) có giá trị lớn hơn hẳn giá trị tuyệt đối của phần tử đứng liền sau nó, tức là $a_i > |a_{i+1}|$.

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
5.0 -3.0 2.5 -1.0 4.0
```

Kết quả:

```text
5.000000 2.500000
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
3
3.0 -3.0 2.0
```

Kết quả:

```text
EMPTY
```

# Giải thích

- **Ví dụ 1:** $5.0 > |-3.0|$ (chọn), $-3.0 \ngtr |2.5|$, $2.5 > |-1.0|$ (chọn), $-1.0 \ngtr |4.0|$.
- **Ví dụ 2:** Không có phần tử nào thỏa mãn nên in `EMPTY`.
- **Ví dụ 3:** $a_0 = 3.0$ không lớn hơn hẳn $|-3.0| = 3.0$; phần tử cuối $a_2$ không có phần tử liền sau. Kết quả là `EMPTY`.
