# 148 - Bài 148: Đảo ngược mảng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy đảo ngược thứ tự các phần tử của mảng ban đầu (thành $a_{n-1}, a_{n-2}, \dots, a_0$).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra mảng đảo ngược gồm $n$ số nguyên cách nhau bởi dấu cách.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
1 2 3 4 5
```

Kết quả:

```text
5 4 3 2 1
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-10 20 0 5
```

Kết quả:

```text
5 0 20 -10
```

# Ví dụ 3

Dữ liệu vào:

```text
1
7
```

Kết quả:

```text
7
```

# Giải thích

- **Ví dụ 1:** Đảo ngược $[1, 2, 3, 4, 5]$ được $[5, 4, 3, 2, 1]$.
- **Ví dụ 2:** Đảo ngược $[-10, 20, 0, 5]$ được $[5, 0, 20, -10]$.
- **Ví dụ 3:** Mảng 1 phần tử khi đảo ngược không đổi.
