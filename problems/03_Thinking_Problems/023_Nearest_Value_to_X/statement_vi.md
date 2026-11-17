# 023 - Bài 23: Giá trị gần x nhất

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$ và một số thực $x$. Hãy tìm phần tử $a_i$ trong mảng có khoảng cách đến $x$ (tức là $|a_i - x|$) **nhỏ nhất**. Nếu có nhiều phần tử cùng đạt khoảng cách nhỏ nhất, hãy chọn phần tử xuất hiện **đầu tiên** trong mảng.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$ và số thực $x$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra giá trị $a_i$ gần $x$ nhất (sai số tuyệt đối hoặc tương đối không quá $10^{-6}$).

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le x, a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5 10.0
1.0 15.5 11.2 8.9 -3.0
```

Kết quả:

```text
8.900000
```

# Ví dụ 2

Dữ liệu vào:

```text
4 5.0
3.0 7.0 1.0 9.0
```

Kết quả:

```text
3.000000
```

# Ví dụ 3

Dữ liệu vào:

```text
3 4.0
-1.0 4.0 10.0
```

Kết quả:

```text
4.000000
```

# Giải thích

- **Ví dụ 1:** $|11.2 - 10.0| = 1.2$ và $|8.9 - 10.0| = 1.1$, nên $8.9$ gần $10.0$ nhất.
- **Ví dụ 2:** $3.0$ và $7.0$ đều cách $5.0$ một khoảng $2.0$; chọn phần tử xuất hiện trước là $3.0$.
- **Ví dụ 3:** $4.0$ trùng với $x$ nên khoảng cách bằng $0$.
