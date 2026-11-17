# 052 - Bài 52: Liệt kê vị trí các số chính phương

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$ (đánh số từ $0$ đến $n - 1$). Hãy liệt kê tất cả các vị trí (chỉ số) mà giá trị tại đó là **số chính phương** (tức $a_i = k^2$ với $k \ge 0$ nguyên).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các chỉ số (tính từ $0$) theo thứ tự tăng dần cách nhau bởi dấu cách, hoặc `EMPTY` nếu không có.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
0 3 9 -4 25
```

Kết quả:

```text
0 2 4
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-1 -4 2 3
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
3
1 16 100
```

Kết quả:

```text
0 1 2
```

# Giải thích

- **Ví dụ 1:** $a_0 = 0 = 0^2$, $a_2 = 9 = 3^2$, $a_4 = 25 = 5^2$. Số $-4 < 0$ không phải số chính phương.
- **Ví dụ 2:** Không có số chính phương nào nên in `EMPTY`.
- **Ví dụ 3:** Cả $1, 16, 100$ đều là số chính phương.
