# 085 - Bài 85: Đếm số lần xuất hiện của x

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$ và một số nguyên $x$. Hãy đếm số lần giá trị $x$ xuất hiện trong mảng.

# Dữ liệu vào

- Dòng đầu tiên chứa hai số nguyên $n$ và $x$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số lần xuất hiện của $x$ trong mảng.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le x, a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6 3
1 3 5 3 2 3
```

Kết quả:

```text
3
```

# Ví dụ 2

Dữ liệu vào:

```text
4 10
1 2 3 4
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
4 -5
-5 -5 5 -5
```

Kết quả:

```text
3
```

# Giải thích

- **Ví dụ 1:** Giá trị $3$ xuất hiện tại các chỉ số $1, 3, 5$ (tổng cộng $3$ lần).
- **Ví dụ 2:** $10$ không xuất hiện lần nào nên kết quả là $0$.
- **Ví dụ 3:** $-5$ xuất hiện $3$ lần (khác với $+5$).
