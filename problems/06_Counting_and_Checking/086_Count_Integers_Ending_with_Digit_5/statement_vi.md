# 086 - Bài 86: Đếm số có chữ số tận cùng bằng 5

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy đếm số lượng phần tử có **chữ số tận cùng** (hàng đơn vị của $|a_i|$) bằng $5$, tức là $|a_i| \bmod 10 = 5$.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số lượng phần tử có chữ số tận cùng bằng $5$.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
5 12 -25 50 105
```

Kết quả:

```text
3
```

# Ví dụ 2

Dữ liệu vào:

```text
4
10 51 550 -14
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
3
-5 15 25
```

Kết quả:

```text
3
```

# Giải thích

- **Ví dụ 1:** Các số tận cùng bằng $5$ là $5, -25, 105$ (có $3$ số).
- **Ví dụ 2:** Không có phần tử nào có hàng đơn vị là $5$ nên kết quả là $0$.
- **Ví dụ 3:** Cả $3$ phần tử đều có chữ số tận cùng bằng $5$.
