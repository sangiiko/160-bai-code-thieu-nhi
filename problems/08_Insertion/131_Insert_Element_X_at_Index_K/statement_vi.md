# 131 - Bài 131: Thêm phần tử x vào vị trí k

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$, một giá trị $x$ và chỉ số $k$ ($0 \le k \le n$, đánh số từ $0$). Hãy chèn phần tử $x$ vào mảng tại vị trí $k$ (đẩy các phần tử từ vị trí $k$ trở về sau sang phải $1$ vị trí).

# Dữ liệu vào

- Dòng đầu tiên chứa ba số nguyên $n, x, k$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra mảng kết quả gồm $n + 1$ số nguyên cách nhau bởi dấu cách.

# Giới hạn

- $1 \le n \le 10^5$
- $0 \le k \le n$
- $-10^9 \le x, a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
4 99 2
10 20 30 40
```

Kết quả:

```text
10 20 99 30 40
```

# Ví dụ 2

Dữ liệu vào:

```text
3 -5 0
1 2 3
```

Kết quả:

```text
-5 1 2 3
```

# Ví dụ 3

Dữ liệu vào:

```text
3 7 3
1 2 3
```

Kết quả:

```text
1 2 3 7
```

# Giải thích

- **Ví dụ 1:** Chèn $99$ vào chỉ số $2$ đẩy $30, 40$ sang phải: $[10, 20, 99, 30, 40]$.
- **Ví dụ 2:** Với $k = 0$, chèn $-5$ vào đầu mảng: $[-5, 1, 2, 3]$.
- **Ví dụ 3:** Với $k = n = 3$, chèn $7$ vào cuối mảng: $[1, 2, 3, 7]$.
