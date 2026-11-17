# 018 - Bài 18: Số nguyên tố lớn nhất

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tìm **số nguyên tố lớn nhất** trong mảng. Nếu mảng không có số nguyên tố nào, in ra `-1`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số nguyên tố lớn nhất trong mảng, hoặc `-1` nếu không có.

# Giới hạn

- $1 \le n \le 10^4$
- $-10^6 \le a_i \le 10^6$

# Ví dụ 1

Dữ liệu vào:

```text
5
4 7 23 19 100
```

Kết quả:

```text
23
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1 4 9 15
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
3
-17 2 1
```

Kết quả:

```text
2
```

# Giải thích

- **Ví dụ 1:** Các số nguyên tố là $7, 23, 19$; lớn nhất là $23$.
- **Ví dụ 2:** Không có số nguyên tố nào nên kết quả là `-1`.
- **Ví dụ 3:** $-17 < 2$ không phải số nguyên tố; số nguyên tố duy nhất là $2$.
