# 092 - Bài 92: Đếm cặp phần tử kề nhau cùng chẵn

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy đếm số lượng cặp phần tử đứng kề nhau $(a_i, a_{i+1})$ ($0 \le i \le n - 2$) sao cho cả $a_i$ và $a_{i+1}$ đều là **số chẵn**.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số lượng cặp kề nhau cùng chẵn.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
2 4 6 1 8
```

Kết quả:

```text
2
```

# Ví dụ 2

Dữ liệu vào:

```text
5
2 1 4 3 6
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
4
0 -2 4 8
```

Kết quả:

```text
3
```

# Giải thích

- **Ví dụ 1:** Có $2$ cặp kề nhau cùng chẵn: $(a_0, a_1) = (2, 4)$ và $(a_1, a_2) = (4, 6)$.
- **Ví dụ 2:** Không có hai số chẵn nào đứng cạnh nhau nên kết quả là $0$.
- **Ví dụ 3:** Cả $3$ cặp liên tiếp $(0, -2), (-2, 4), (4, 8)$ đều cùng chẵn.
