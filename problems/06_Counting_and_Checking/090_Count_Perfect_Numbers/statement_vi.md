# 090 - Bài 90: Đếm số hoàn thiện

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy đếm số lượng **số hoàn thiện** có trong mảng (số nguyên dương bằng tổng các ước nguyên dương thực sự của nó, như $6, 28, 496, \dots$).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số lượng số hoàn thiện trong mảng.

# Giới hạn

- $1 \le n \le 10^4$
- $-10^6 \le a_i \le 10^6$

# Ví dụ 1

Dữ liệu vào:

```text
5
6 12 28 10 496
```

Kết quả:

```text
3
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-6 0 1 12
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
3
6 6 28
```

Kết quả:

```text
3
```

# Giải thích

- **Ví dụ 1:** Các số hoàn thiện là $6, 28, 496$ (có $3$ số).
- **Ví dụ 2:** Không có số hoàn thiện nào nên kết quả là $0$.
- **Ví dụ 3:** Có $3$ phần tử là số hoàn thiện ($6, 6, 28$).
