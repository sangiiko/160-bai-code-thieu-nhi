# 108 - Bài 108: Kiểm tra mảng có số nguyên tố

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy kiểm tra xem trong mảng có tồn tại ít nhất một **số nguyên tố** hay không.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra `1` nếu mảng có số nguyên tố, ngược lại in ra `0`.

# Giới hạn

- $1 \le n \le 10^4$
- $-10^6 \le a_i \le 10^6$

# Ví dụ 1

Dữ liệu vào:

```text
4
4 6 8 11
```

Kết quả:

```text
1
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-7 0 1 9
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
1
2
```

Kết quả:

```text
1
```

# Giải thích

- **Ví dụ 1:** Có số nguyên tố $11$ nên kết quả là `1`.
- **Ví dụ 2:** $-7, 0, 1, 9$ đều không phải số nguyên tố nên kết quả là `0`.
- **Ví dụ 3:** $2$ là số nguyên tố nên kết quả là `1`.
