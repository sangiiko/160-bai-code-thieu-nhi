# 157 - Bài 157: Làm tròn các phần tử số thực về số nguyên gần nhất

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy thay tất cả phần tử trong mảng bằng **số nguyên gần nó nhất** (quy tắc làm tròn chuẩn nửa ra xa $0$, tức $1.5 \to 2$ và $-1.5 \to -2$, tương ứng hàm `llround`).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra $n$ số nguyên sau khi làm tròn, cách nhau bởi dấu cách.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6
1.4 1.5 -1.5 -2.3 -2.6 3.9
```

Kết quả:

```text
1 2 -2 -2 -3 4
```

# Ví dụ 2

Dữ liệu vào:

```text
3
0.49 -0.49 0.0
```

Kết quả:

```text
0 0 0
```

# Ví dụ 3

Dữ liệu vào:

```text
3
2.5 -2.5 10.0
```

Kết quả:

```text
3 -3 10
```

# Giải thích

- **Ví dụ 1:** $1.4 \to 1$, $1.5 \to 2$, $-1.5 \to -2$, $-2.3 \to -2$, $-2.6 \to -3$, $3.9 \to 4$.
- **Ví dụ 2:** Cả $0.49$ và $-0.49$ đều gần $0$ nhất.
- **Ví dụ 3:** Làm tròn nửa ra xa $0$: $2.5 \to 3$ và $-2.5 \to -3$.
