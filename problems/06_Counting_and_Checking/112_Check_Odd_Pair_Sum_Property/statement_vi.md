# 112 - Bài 112: Kiểm tra mảng có tính chất lẻ

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Một mảng số nguyên $a$ gồm $n$ phần tử được gọi là có **tính chất lẻ** nếu tổng của mọi cặp hai phần tử liên tiếp $a_i + a_{i+1}$ ($0 \le i \le n - 2$) luôn là một số lẻ (tương đương hai phần tử kề nhau luôn khác tính chẵn lẻ).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra `1` nếu mảng có tính chất lẻ, ngược lại in ra `0`.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
4
2 3 8 5
```

Kết quả:

```text
1
```

# Ví dụ 2

Dữ liệu vào:

```text
4
2 3 5 8
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
1
10
```

Kết quả:

```text
1
```

# Giải thích

- **Ví dụ 1:** Các tổng liên tiếp: $2+3=5$, $3+8=11$, $8+5=13$ đều là số lẻ (`1`).
- **Ví dụ 2:** $3 + 5 = 8$ là số chẵn nên không thỏa mãn (`0`).
- **Ví dụ 3:** Mảng có $1$ phần tử không có cặp liên tiếp nào vi phạm nên mặc định thỏa mãn (`1`).
