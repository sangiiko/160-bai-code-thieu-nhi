# 110 - Bài 110: Kiểm tra mảng toàn số chẵn

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy kiểm tra xem **tất cả** các phần tử trong mảng có đều là số chẵn hay không.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra `1` nếu mảng toàn số chẵn, ngược lại in ra `0`.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
4
2 4 -6 0
```

Kết quả:

```text
1
```

# Ví dụ 2

Dữ liệu vào:

```text
4
2 4 6 1
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
1
-8
```

Kết quả:

```text
1
```

# Giải thích

- **Ví dụ 1:** Cả $4$ phần tử đều chia hết cho $2$ (`1`).
- **Ví dụ 2:** Phần tử cuối cùng $1$ là số lẻ (`0`).
- **Ví dụ 3:** $-8$ là số chẵn (`1`).
