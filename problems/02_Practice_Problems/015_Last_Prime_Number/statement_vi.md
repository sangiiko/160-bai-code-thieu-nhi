# 015 - Bài 15: Số nguyên tố cuối cùng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tìm **số nguyên tố** xuất hiện cuối cùng trong mảng. Nếu mảng không có số nguyên tố nào, in ra `-1`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số nguyên tố cuối cùng trong mảng, hoặc `-1` nếu không có.

# Giới hạn

- $1 \le n \le 10^4$
- $-10^6 \le a_i \le 10^6$

# Ví dụ 1

Dữ liệu vào:

```text
6
2 5 8 17 10 12
```

Kết quả:

```text
17
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1 4 6 -5
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
3
19 4 2
```

Kết quả:

```text
2
```

# Giải thích

- **Ví dụ 1:** Các số nguyên tố là $2, 5, 17$; số nguyên tố cuối cùng là $17$.
- **Ví dụ 2:** Không có số nguyên tố nào nên in `-1`.
- **Ví dụ 3:** Số nguyên tố cuối cùng là $2$.
