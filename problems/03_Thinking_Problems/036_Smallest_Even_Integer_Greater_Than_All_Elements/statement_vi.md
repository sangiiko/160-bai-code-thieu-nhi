# 036 - Bài 36: Số chẵn nhỏ nhất lớn hơn mọi phần tử

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tìm **số chẵn nhỏ nhất** lớn hơn hẳn mọi giá trị có trong mảng (tức lớn hơn $\max(a)$).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra một số nguyên duy nhất là số chẵn nhỏ nhất lớn hơn mọi phần tử của mảng.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
4
3 10 7 8
```

Kết quả:

```text
12
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1 5 9 3
```

Kết quả:

```text
10
```

# Ví dụ 3

Dữ liệu vào:

```text
3
-10 -5 -3
```

Kết quả:

```text
-2
```

# Giải thích

- **Ví dụ 1:** Giá trị lớn nhất trong mảng là $10$; số chẵn nhỏ nhất $> 10$ là $12$.
- **Ví dụ 2:** Giá trị lớn nhất là $9$; số chẵn nhỏ nhất $> 9$ là $10$.
- **Ví dụ 3:** Giá trị lớn nhất là $-3$; số chẵn nhỏ nhất $> -3$ là $-2$.
