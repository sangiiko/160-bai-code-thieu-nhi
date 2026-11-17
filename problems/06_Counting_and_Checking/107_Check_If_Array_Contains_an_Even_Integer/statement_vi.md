# 107 - Bài 107: Kiểm tra mảng có số chẵn

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy kiểm tra xem trong mảng có tồn tại ít nhất một **số chẵn** hay không.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra `1` nếu mảng có số chẵn, ngược lại in ra `0`.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
4
1 3 5 7
```

Kết quả:

```text
0
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1 3 0 5
```

Kết quả:

```text
1
```

# Ví dụ 3

Dữ liệu vào:

```text
3
-4 1 3
```

Kết quả:

```text
1
```

# Giải thích

- **Ví dụ 1:** Mảng toàn số lẻ nên kết quả là `0`.
- **Ví dụ 2:** Số $0$ là số chẵn nên kết quả là `1`.
- **Ví dụ 3:** $-4$ là số chẵn nên kết quả là `1`.
