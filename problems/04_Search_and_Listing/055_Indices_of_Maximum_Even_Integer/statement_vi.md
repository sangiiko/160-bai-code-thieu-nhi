# 055 - Bài 55: Liệt kê vị trí giá trị chẵn lớn nhất

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$ (đánh số từ $0$ đến $n - 1$). Hãy tìm giá trị chẵn lớn nhất trong mảng và liệt kê tất cả các vị trí (chỉ số) $i$ mà $a_i$ bằng giá trị chẵn lớn nhất đó. Nếu mảng không có số chẵn nào, in ra `-1`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các chỉ số (tính từ $0$) thỏa mãn theo thứ tự tăng dần cách nhau bởi dấu cách, hoặc `-1` nếu mảng không có số chẵn.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6
8 3 8 5 4 7
```

Kết quả:

```text
0 2
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1 3 5 -7
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
5
-4 -2 -4 1 -2
```

Kết quả:

```text
1 4
```

# Giải thích

- **Ví dụ 1:** Giá trị chẵn lớn nhất là $8$, xuất hiện tại các chỉ số $0$ và $2$.
- **Ví dụ 2:** Mảng toàn số lẻ nên kết quả là `-1`.
- **Ví dụ 3:** Giá trị chẵn lớn nhất là $-2$, tại chỉ số $1$ và $4$.
