# 118 - Bài 118: Kiểm tra mảng a nằm trong mảng b

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho hai mảng số nguyên $a$ (gồm $n$ phần tử) và $b$ (gồm $m$ phần tử). Hãy kiểm tra xem **tất cả** các phần tử có mặt trong mảng $a$ có đều xuất hiện trong mảng $b$ hay không (không yêu cầu thứ tự hay số lần xuất hiện).

# Dữ liệu vào

- Dòng đầu tiên chứa hai số nguyên dương $n$ và $m$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, \dots, a_{n-1}$.
- Dòng thứ ba chứa $m$ số nguyên $b_0, \dots, b_{m-1}$.

# Kết quả

- In ra `1` nếu mọi phần tử của $a$ đều nằm trong $b$, ngược lại in ra `0`.

# Giới hạn

- $1 \le n, m \le 10^5$
- $-10^9 \le a_i, b_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
3 5
2 5 2
1 2 3 4 5
```

Kết quả:

```text
1
```

# Ví dụ 2

Dữ liệu vào:

```text
3 4
2 6 3
1 2 3 4
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
2 2
-5 0
0 -5
```

Kết quả:

```text
1
```

# Giải thích

- **Ví dụ 1:** Cả $2$ và $5$ đều có mặt trong mảng $b$ (`1`).
- **Ví dụ 2:** Phần tử $6$ trong $a$ không xuất hiện trong $b$ (`0`).
- **Ví dụ 3:** Các phần tử $-5$ và $0$ đều có trong $b$ (`1`).
