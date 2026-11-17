# 082 - Bài 82: Đếm số lượng số chẵn

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy đếm số lượng số chẵn có trong mảng.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra một số nguyên duy nhất là số lượng số chẵn trong mảng.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
2 3 4 -6 7
```

Kết quả:

```text
3
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1 3 -5 9
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
4
0 -2 4 10
```

Kết quả:

```text
4
```

# Giải thích

- **Ví dụ 1:** Các số chẵn là $2, 4, -6$ (có $3$ số).
- **Ví dụ 2:** Không có số chẵn nào nên kết quả là $0$.
- **Ví dụ 3:** Cả $4$ số (kể cả $0$ và số âm $-2$) đều là số chẵn.
