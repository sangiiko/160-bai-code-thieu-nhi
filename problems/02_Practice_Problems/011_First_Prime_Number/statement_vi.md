# 011 - Bài 11: Số nguyên tố đầu tiên

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tìm **số nguyên tố** đầu tiên xuất hiện trong mảng. Nếu mảng không chứa số nguyên tố nào, in ra `-1`.

*Định nghĩa:* Số nguyên tố là số nguyên lớn hơn hoặc bằng $2$ và chỉ có đúng hai ước nguyên dương là $1$ và chính nó.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số nguyên tố đầu tiên trong mảng, hoặc `-1` nếu không tồn tại.

# Giới hạn

- $1 \le n \le 10^4$
- $-10^6 \le a_i \le 10^6$

# Ví dụ 1

Dữ liệu vào:

```text
6
1 4 9 11 7 13
```

Kết quả:

```text
11
```

# Ví dụ 2

Dữ liệu vào:

```text
5
-7 -2 0 1 15
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
4
2 3 5 7
```

Kết quả:

```text
2
```

# Giải thích

- **Ví dụ 1:** $1, 4, 9$ không phải số nguyên tố; số nguyên tố đầu tiên là $11$.
- **Ví dụ 2:** Số âm, $0, 1, 15$ đều không phải số nguyên tố nên kết quả là `-1`.
- **Ví dụ 3:** Số nguyên tố đầu tiên là $2$.
