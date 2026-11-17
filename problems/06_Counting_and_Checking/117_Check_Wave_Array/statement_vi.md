# 117 - Bài 117: Kiểm tra mảng dạng sóng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Một mảng $a$ gồm $n$ số nguyên ($n \ge 3$) được gọi là **dạng sóng** nếu mọi phần tử nằm bên trong mảng $a_i$ ($1 \le i \le n - 2$) đều lớn hơn hẳn cả hai phần tử xung quanh nó ($a_{i-1} < a_i > a_{i+1}$) **hoặc** nhỏ hơn hẳn cả hai phần tử xung quanh nó ($a_{i-1} > a_i < a_{i+1}$). Hãy kiểm tra mảng có dạng sóng hay không.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra `1` nếu mảng có dạng sóng, ngược lại in ra `0`.

# Giới hạn

- $3 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
1 5 2 8 3
```

Kết quả:

```text
1
```

# Ví dụ 2

Dữ liệu vào:

```text
5
1 3 5 2 4
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
4
5 2 2 5
```

Kết quả:

```text
0
```

# Giải thích

- **Ví dụ 1:** $5 > 1, 2$; $2 < 5, 8$; $8 > 2, 3$ — mọi phần tử bên trong đều là đỉnh hoặc đáy (`1`).
- **Ví dụ 2:** Tại $i = 1$: $1 < 3 < 5$ không phải đỉnh cũng không phải đáy (`0`).
- **Ví dụ 3:** Hai phần tử kề nhau bằng $2$ nên không lớn hơn/nhỏ hơn hẳn (`0`).
