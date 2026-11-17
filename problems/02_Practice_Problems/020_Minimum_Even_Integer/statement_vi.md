# 020 - Bài 20: Giá trị chẵn nhỏ nhất

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tìm giá trị **chẵn nhỏ nhất** trong mảng. Nếu mảng không có số chẵn nào, in ra `-1`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số chẵn nhỏ nhất trong mảng, hoặc `-1` nếu mảng không chứa số chẵn.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
7 -4 2 -10 9
```

Kết quả:

```text
-10
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1 -3 5 7
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
4
0 2 4 6
```

Kết quả:

```text
0
```

# Giải thích

- **Ví dụ 1:** Các số chẵn là $-4, 2, -10$; nhỏ nhất là $-10$.
- **Ví dụ 2:** Mảng toàn số lẻ nên in `-1`.
- **Ví dụ 3:** Số chẵn nhỏ nhất là $0$.
