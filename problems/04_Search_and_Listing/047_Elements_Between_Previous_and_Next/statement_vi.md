# 047 - Bài 47: Liệt kê giá trị giữa |trước| và |sau|

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy liệt kê tất cả các phần tử $a_i$ ($1 \le i \le n - 2$) thỏa mãn đồng thời hai điều kiện:
1. $a_i$ nhỏ hơn hẳn trị tuyệt đối của giá trị đứng liền sau nó ($a_i < |a_{i+1}|$).
2. $a_i$ lớn hơn hẳn trị tuyệt đối của giá trị đứng liền trước nó ($a_i > |a_{i-1}|$).

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
-2.0 3.5 -5.0 4.0 1.0
```

Kết quả:

```text
3.500000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
5.0 4.0 3.0 2.0
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
6
1.0 2.0 -3.0 4.0 -5.0 6.0
```

Kết quả:

```text
2.000000 4.000000
```

# Giải thích

- **Ví dụ 1:** Tại $i = 1$: $|-2.0| = 2.0 < 3.5 < |-5.0| = 5.0$ (thỏa mãn).
- **Ví dụ 2:** Không có phần tử nào thỏa mãn cả hai điều kiện nên in `EMPTY`.
- **Ví dụ 3:** Tại $i = 1$: $|1| < 2 < |-3|$ (chọn $2.0$); tại $i = 3$: $|-3| < 4 < |-5|$ (chọn $4.0$).
