# 008 - Bài 8: Vị trí giá trị dương nhỏ nhất

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$ (đánh số từ $0$ đến $n - 1$). Hãy tìm vị trí (chỉ số) của phần tử **dương** ($a_i > 0$) có giá trị nhỏ nhất trong mảng. Nếu có nhiều vị trí cùng đạt giá trị dương nhỏ nhất, chọn **chỉ số nhỏ nhất**. Nếu mảng không có phần tử dương, in ra `-1`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra chỉ số (tính từ $0$) của giá trị dương nhỏ nhất, hoặc `-1` nếu mảng không có số dương.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6
-5.0 3.2 0.0 1.25 4.8 1.25
```

Kết quả:

```text
3
```

# Ví dụ 2

Dữ liệu vào:

```text
3
0.0 -2.5 -0.1
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
4
10.0 5.0 2.0 1.0
```

Kết quả:

```text
3
```

# Giải thích

- **Ví dụ 1:** Giá trị dương nhỏ nhất là $1.25$, xuất hiện ở chỉ số $3$ và $5$; chỉ số nhỏ nhất là $3$.
- **Ví dụ 2:** Không có giá trị dương nên in `-1`.
- **Ví dụ 3:** Giá trị dương nhỏ nhất là $1.0$ tại chỉ số $3$.
