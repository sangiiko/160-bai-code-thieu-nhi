# 063 - Bài 63: Liệt kê số nguyên có chữ số đầu lẻ (2)

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy liệt kê tất cả các giá trị trong mảng có chữ số đầu tiên (chữ số đầu của $|a_i|$) là chữ số lẻ theo thứ tự xuất hiện.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các phần tử thỏa mãn cách nhau bởi dấu cách, hoặc `EMPTY` nếu không có.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
4
70 81 -53 20
```

Kết quả:

```text
70 -53
```

# Ví dụ 2

Dữ liệu vào:

```text
3
2 40 600
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
3
9 31 102
```

Kết quả:

```text
9 31 102
```

# Giải thích

- **Ví dụ 1:** $70$ bắt đầu bằng $7$ và $-53$ bắt đầu bằng $5$.
- **Ví dụ 2:** Không có phần tử nào bắt đầu bằng chữ số lẻ nên in `EMPTY`.
- **Ví dụ 3:** Cả ba số đều bắt đầu bằng chữ số lẻ ($9, 3, 1$).
