# 005 - Bài 5: Vị trí giá trị chẵn đầu tiên

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$ (đánh số từ $0$ đến $n - 1$). Hãy tìm vị trí (chỉ số) của phần tử chẵn **đầu tiên** trong mảng. Nếu mảng không chứa số chẵn nào, in ra `-1`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra chỉ số (tính từ $0$) của phần tử chẵn đầu tiên, hoặc `-1` nếu không tồn tại.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
1 7 -4 9 6
```

Kết quả:

```text
2
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-1 3 5 11
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
4
0 1 2 3
```

Kết quả:

```text
0
```

# Giải thích

- **Ví dụ 1:** $a_0 = 1$ và $a_1 = 7$ là số lẻ; phần tử chẵn đầu tiên là $a_2 = -4$ tại chỉ số $2$.
- **Ví dụ 2:** Mảng không có số chẵn nên kết quả là `-1`.
- **Ví dụ 3:** $a_0 = 0$ là số chẵn nên vị trí đầu tiên là $0$.
