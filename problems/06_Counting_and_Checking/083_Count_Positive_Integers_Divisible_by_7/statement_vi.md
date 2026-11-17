# 083 - Bài 83: Đếm số dương chia hết cho 7

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy đếm số lượng phần tử thỏa mãn đồng thời hai điều kiện: mang giá trị **dương** ($a_i > 0$) và chia hết cho $7$.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số lượng phần tử thỏa mãn điều kiện.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6
-7 0 7 14 20 21
```

Kết quả:

```text
3
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-14 0 1 8
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
3
7 7 7
```

Kết quả:

```text
3
```

# Giải thích

- **Ví dụ 1:** $-7 < 0$ và $0$ không dương; các số dương chia hết cho $7$ là $7, 14, 21$ (có $3$ số).
- **Ví dụ 2:** Không có số dương nào chia hết cho $7$ nên kết quả là $0$.
- **Ví dụ 3:** Cả $3$ phần tử đều là $7$ nên kết quả là $3$.
