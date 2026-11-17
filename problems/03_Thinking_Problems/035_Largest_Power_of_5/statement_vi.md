# 035 - Bài 35: Giá trị lớn nhất có dạng 5^k

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tìm giá trị **lớn nhất** trong mảng có dạng $5^k$ với $k$ là số nguyên không âm ($k \ge 0$, tức là $\{1, 5, 25, 125, \dots\}$). Nếu mảng không tồn tại giá trị dạng $5^k$, in ra `0`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra giá trị lớn nhất có dạng $5^k$, hoặc `0` nếu không có.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
10 25 125 5 50
```

Kết quả:

```text
125
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-25 0 10 15
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
3
2 1 3
```

Kết quả:

```text
1
```

# Giải thích

- **Ví dụ 1:** Các số có dạng $5^k$ là $25, 125, 5$; lớn nhất là $125 = 5^3$.
- **Ví dụ 2:** Không có số nào là lũy thừa của $5$ nên in `0`.
- **Ví dụ 3:** $1 = 5^0$ là giá trị lớn nhất dạng $5^k$.
