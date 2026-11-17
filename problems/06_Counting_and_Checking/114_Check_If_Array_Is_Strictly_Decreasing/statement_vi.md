# 114 - Bài 114: Kiểm tra mảng giảm dần

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy kiểm tra xem mảng có **giảm dần nghiêm ngặt** ($a_0 > a_1 > \dots > a_{n-1}$) hay không.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra `1` nếu mảng giảm dần nghiêm ngặt, ngược lại in ra `0`.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
4
9.0 5.5 2.1 -1.0
```

Kết quả:

```text
1
```

# Ví dụ 2

Dữ liệu vào:

```text
4
5.0 5.0 3.0 1.0
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
3
1.0 2.0 0.0
```

Kết quả:

```text
0
```

# Giải thích

- **Ví dụ 1:** $9.0 > 5.5 > 2.1 > -1.0$ (`1`).
- **Ví dụ 2:** $a_0 = a_1 = 5.0$ không giảm nghiêm ngặt (`0`).
- **Ví dụ 3:** $1.0 < 2.0$ vi phạm tính giảm dần (`0`).
