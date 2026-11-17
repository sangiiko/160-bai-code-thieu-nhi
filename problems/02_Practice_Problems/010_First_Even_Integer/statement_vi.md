# 010 - Bài 10: Số chẵn đầu tiên trong mảng số nguyên

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tìm giá trị chẵn **đầu tiên** xuất hiện trong mảng. Nếu mảng không có số chẵn nào, in ra `-1`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số chẵn đầu tiên tìm được, hoặc `-1` nếu không có.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
3 7 -12 4 9
```

Kết quả:

```text
-12
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1 3 -5 9
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
4
-7 0 2 4
```

Kết quả:

```text
0
```

# Giải thích

- **Ví dụ 1:** $3$ và $7$ là số lẻ, nên số chẵn đầu tiên là $-12$.
- **Ví dụ 2:** Mảng không có số chẵn nào nên kết quả là `-1`.
- **Ví dụ 3:** Số $0$ là số chẵn đầu tiên trong mảng.
