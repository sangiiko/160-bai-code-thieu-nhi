# 141 - Bài 141: Xóa tất cả phần tử trùng với x

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$ và một số nguyên $x$. Hãy xóa **tất cả** các phần tử có giá trị bằng $x$ khỏi mảng, giữ nguyên thứ tự các phần tử còn lại.

# Dữ liệu vào

- Dòng đầu tiên chứa hai số nguyên $n$ và $x$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các phần tử còn lại cách nhau bởi dấu cách, hoặc `EMPTY` nếu mảng trở nên rỗng.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le x, a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6 5
5 2 5 8 5 3
```

Kết quả:

```text
2 8 3
```

# Ví dụ 2

Dữ liệu vào:

```text
4 7
7 7 7 7
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
4 10
1 2 3 4
```

Kết quả:

```text
1 2 3 4
```

# Giải thích

- **Ví dụ 1:** Xóa cả ba lần xuất hiện của $5$, còn $[2, 8, 3]$.
- **Ví dụ 2:** Mọi phần tử đều bằng $7$ nên kết quả là `EMPTY`.
- **Ví dụ 3:** $10$ không xuất hiện nên mảng giữ nguyên.
