# 066 - Bài 66: Tổng các phần tử trong mảng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy tính tổng tất cả các phần tử có trong mảng.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra tổng các phần tử trong mảng (sai số tuyệt đối hoặc tương đối không quá $10^{-6}$).

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
4
1.5 2.5 -1.0 3.0
```

Kết quả:

```text
6.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
3
-5.0 2.0 3.0
```

Kết quả:

```text
0.000000
```

# Ví dụ 3

Dữ liệu vào:

```text
1
7.25
```

Kết quả:

```text
7.250000
```

# Giải thích

- **Ví dụ 1:** $1.5 + 2.5 + (-1.0) + 3.0 = 6.0$.
- **Ví dụ 2:** $-5.0 + 2.0 + 3.0 = 0.0$.
- **Ví dụ 3:** Tổng bằng $7.25$.
