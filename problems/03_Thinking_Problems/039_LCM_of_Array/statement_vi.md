# 039 - Bài 39: Bội chung nhỏ nhất của mảng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên dương $a_0, a_1, \dots, a_{n-1}$. Hãy tìm bội chung nhỏ nhất (BCNN / $\operatorname{lcm}$) của tất cả các phần tử trong mảng.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên dương $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra một số nguyên dương là $\operatorname{lcm}(a_0, a_1, \dots, a_{n-1})$.

# Giới hạn

- $1 \le n \le 20$
- $1 \le a_i \le 10^4$, đảm bảo kết quả nằm trong kiểu số nguyên 64-bit có dấu ($\le 9 \times 10^{18}$).

# Ví dụ 1

Dữ liệu vào:

```text
4
4 6 8 12
```

Kết quả:

```text
24
```

# Ví dụ 2

Dữ liệu vào:

```text
3
7 11 13
```

Kết quả:

```text
1001
```

# Ví dụ 3

Dữ liệu vào:

```text
1
15
```

Kết quả:

```text
15
```

# Giải thích

- **Ví dụ 1:** $\operatorname{lcm}(4, 6, 8, 12) = 24$.
- **Ví dụ 2:** $7, 11, 13$ đôi một nguyên tố cùng nhau nên BCNN là $7 \times 11 \times 13 = 1001$.
- **Ví dụ 3:** Mảng có 1 phần tử $15$ nên kết quả là $15$.
