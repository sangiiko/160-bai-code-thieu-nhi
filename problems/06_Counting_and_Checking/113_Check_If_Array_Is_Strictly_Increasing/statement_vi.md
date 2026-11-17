# 113 - Bài 113: Kiểm tra mảng tăng dần

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy kiểm tra xem mảng có **tăng dần nghiêm ngặt** ($a_0 < a_1 < \dots < a_{n-1}$) hay không.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra `1` nếu mảng tăng dần nghiêm ngặt, ngược lại in ra `0`.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
4
-2.0 0.5 3.0 7.5
```

Kết quả:

```text
1
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1.0 2.5 2.5 4.0
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
1
5.0
```

Kết quả:

```text
1
```

# Giải thích

- **Ví dụ 1:** $-2.0 < 0.5 < 3.0 < 7.5$ (`1`).
- **Ví dụ 2:** $a_1 = a_2 = 2.5$ không tăng nghiêm ngặt (`0`).
- **Ví dụ 3:** Mảng 1 phần tử luôn thỏa mãn (`1`).
