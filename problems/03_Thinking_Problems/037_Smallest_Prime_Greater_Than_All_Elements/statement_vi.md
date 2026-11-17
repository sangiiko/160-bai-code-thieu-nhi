# 037 - Bài 37: Số nguyên tố nhỏ nhất lớn hơn mọi phần tử

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tìm **số nguyên tố nhỏ nhất** lớn hơn hẳn mọi giá trị có trong mảng.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số nguyên tố nhỏ nhất lớn hơn $\max(a)$.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^6 \le a_i \le 10^6$

# Ví dụ 1

Dữ liệu vào:

```text
4
3 10 7 8
```

Kết quả:

```text
11
```

# Ví dụ 2

Dữ liệu vào:

```text
3
-5 0 1
```

Kết quả:

```text
2
```

# Ví dụ 3

Dữ liệu vào:

```text
3
11 13 17
```

Kết quả:

```text
19
```

# Giải thích

- **Ví dụ 1:** Giá trị lớn nhất là $10$; số nguyên tố nhỏ nhất $> 10$ là $11$.
- **Ví dụ 2:** Giá trị lớn nhất là $1$; số nguyên tố nhỏ nhất $> 1$ là $2$.
- **Ví dụ 3:** Giá trị lớn nhất là $17$; số nguyên tố tiếp theo là $19$.
