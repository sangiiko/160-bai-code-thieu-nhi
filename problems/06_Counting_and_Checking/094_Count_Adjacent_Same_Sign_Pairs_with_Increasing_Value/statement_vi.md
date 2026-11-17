# 094 - Bài 94: Đếm cặp kề nhau cùng dấu và trị tuyệt đối tăng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy đếm số lượng cặp phần tử kề nhau $(a_i, a_{i+1})$ ($0 \le i \le n - 2$) sao cho phần tử đứng sau $a_{i+1}$ **cùng dấu** với phần tử đứng trước $a_i$ ($a_i \cdot a_{i+1} > 0$) và có giá trị tuyệt đối lớn hơn hẳn ($|a_{i+1}| > |a_i|$).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số lượng cặp thỏa mãn điều kiện.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
-2.0 -5.0 -3.0 1.0 4.0
```

Kết quả:

```text
2
```

# Ví dụ 2

Dữ liệu vào:

```text
4
5.0 3.0 0.0 -2.0
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
4
1.0 2.0 2.0 5.0
```

Kết quả:

```text
2
```

# Giải thích

- **Ví dụ 1:** $(-2.0, -5.0)$ cùng dấu âm và $|-5.0| > |-2.0|$; $(1.0, 4.0)$ cùng dấu dương và $|4.0| > |1.0|$. Tổng cộng $2$ cặp.
- **Ví dụ 2:** Không có cặp nào thỏa mãn nên kết quả là $0$.
- **Ví dụ 3:** $(1.0, 2.0)$ và $(2.0, 5.0)$ thỏa mãn ($|2.0| \ngtr |2.0|$ nên cặp giữa không tính).
