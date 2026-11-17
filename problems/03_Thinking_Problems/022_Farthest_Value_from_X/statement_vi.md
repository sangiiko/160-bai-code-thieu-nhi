# 022 - Bài 22: Giá trị xa x nhất

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$ và một số thực $x$. Hãy tìm phần tử $a_i$ trong mảng có khoảng cách đến $x$ (tức là $|a_i - x|$) **lớn nhất**. Nếu có nhiều phần tử cùng đạt khoảng cách lớn nhất, hãy chọn phần tử xuất hiện **đầu tiên** trong mảng.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$ và số thực $x$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra giá trị $a_i$ xa $x$ nhất (sai số tuyệt đối hoặc tương đối không quá $10^{-6}$).

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le x, a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5 10.0
1.0 15.5 22.0 8.0 -3.0
```

Kết quả:

```text
-3.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
4 0.0
-5.0 5.0 2.0 -2.0
```

Kết quả:

```text
-5.000000
```

# Ví dụ 3

Dữ liệu vào:

```text
1 7.5
7.5
```

Kết quả:

```text
7.500000
```

# Giải thích

- **Ví dụ 1:** Khoảng cách lần lượt là $|1-10|=9$, $|15.5-10|=5.5$, $|22-10|=12$, $|8-10|=2$, $|-3-10|=13$. Xa nhất là $-3.0$.
- **Ví dụ 2:** $-5.0$ và $5.0$ cùng có khoảng cách bằng $5.0$ đến $0.0$; chọn phần tử đầu tiên là $-5.0$.
- **Ví dụ 3:** Chỉ có một phần tử duy nhất là $7.5$.
