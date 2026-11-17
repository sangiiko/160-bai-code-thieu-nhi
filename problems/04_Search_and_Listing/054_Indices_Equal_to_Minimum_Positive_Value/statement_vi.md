# 054 - Bài 54: Liệt kê vị trí bằng giá trị dương nhỏ nhất

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$ (đánh số từ $0$ đến $n - 1$). Gọi $v$ là giá trị **dương** ($a_i > 0$) nhỏ nhất trong mảng. Hãy liệt kê tất cả các vị trí (chỉ số) $i$ sao cho $a_i = v$. Nếu mảng không có số dương nào, in ra `-1`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các chỉ số (tính từ $0$) thỏa mãn theo thứ tự tăng dần cách nhau bởi dấu cách, hoặc `-1` nếu mảng không có giá trị dương.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
-1.0 2.5 5.0 2.5 0.0
```

Kết quả:

```text
1 3
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-3.0 0.0 -1.5 -0.2
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
4
1.0 1.0 1.0 2.0
```

Kết quả:

```text
0 1 2
```

# Giải thích

- **Ví dụ 1:** Giá trị dương nhỏ nhất là $2.5$, xuất hiện tại các chỉ số $1$ và $3$.
- **Ví dụ 2:** Không có giá trị dương nào nên in `-1`.
- **Ví dụ 3:** Giá trị dương nhỏ nhất là $1.0$ tại các chỉ số $0, 1, 2$.
