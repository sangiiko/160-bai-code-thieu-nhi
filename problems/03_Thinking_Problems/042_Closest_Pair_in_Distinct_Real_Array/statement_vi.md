# 042 - Bài 42: Hai giá trị gần nhau nhất trong mảng phân biệt

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực **đôi một phân biệt** ($n > 2$). Hãy tìm hai phần tử $x, y$ ($x < y$) trong mảng có hiệu $|y - x|$ nhỏ nhất. Nếu có nhiều cặp cùng đạt khoảng cách nhỏ nhất, chọn cặp có giá trị $x$ nhỏ nhất.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên $n$.
- Dòng thứ hai chứa $n$ số thực đôi một phân biệt $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra hai số thực $x$ và $y$ ($x < y$) cách nhau bởi một dấu cách (sai số tuyệt đối hoặc tương đối không quá $10^{-6}$).

# Giới hạn

- $3 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$, các phần tử đôi một phân biệt.

# Ví dụ 1

Dữ liệu vào:

```text
5
1.5 9.0 3.2 3.8 7.1
```

Kết quả:

```text
3.200000 3.800000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1.0 2.0 3.0 5.0
```

Kết quả:

```text
1.000000 2.000000
```

# Ví dụ 3

Dữ liệu vào:

```text
3
-5.0 0.0 3.0
```

Kết quả:

```text
0.000000 3.000000
```

# Giải thích

- **Ví dụ 1:** Khi sắp xếp tăng dần được $[1.5, 3.2, 3.8, 7.1, 9.0]$; khoảng cách nhỏ nhất là $3.8 - 3.2 = 0.6$.
- **Ví dụ 2:** Hai cặp $(1.0, 2.0)$ và $(2.0, 3.0)$ cùng có khoảng cách $1.0$; chọn cặp có $x$ nhỏ nhất là $(1.0, 2.0)$.
- **Ví dụ 3:** Khoảng cách giữa $0.0$ và $3.0$ là $3.0$ (nhỏ hơn $0.0 - (-5.0) = 5.0$).
