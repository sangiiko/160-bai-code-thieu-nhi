# 003 - Bài 3: Số chẵn cuối cùng trong mảng số nguyên

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tìm số chẵn xuất hiện **cuối cùng** trong mảng (có chỉ số lớn nhất). Nếu mảng không có số chẵn nào, in ra `-1`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra giá trị của số chẵn cuối cùng trong mảng, hoặc `-1` nếu mảng toàn số lẻ.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6
3 4 7 -8 10 5
```

Kết quả:

```text
10
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1 -3 5 99
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
5
2 4 6 8 0
```

Kết quả:

```text
0
```

# Giải thích

- **Ví dụ 1:** Các số chẵn trong mảng theo thứ tự là $4, -8, 10$; số chẵn cuối cùng là $10$.
- **Ví dụ 2:** Cả $4$ phần tử đều lẻ nên kết quả là `-1`.
- **Ví dụ 3:** Số $0$ chia hết cho $2$ nên là số chẵn; phần tử chẵn cuối cùng là $0$.
