# 140 - Bài 140: Xóa tất cả số chính phương

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy xóa tất cả các **số chính phương** ($a_i = k^2$ với $k \ge 0$ nguyên) khỏi mảng, giữ nguyên thứ tự của các phần tử còn lại.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các phần tử còn lại cách nhau bởi dấu cách, hoặc `EMPTY` nếu toàn bộ mảng bị xóa.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
1 3 4 7 16
```

Kết quả:

```text
3 7
```

# Ví dụ 2

Dữ liệu vào:

```text
4
0 1 9 25
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
4
-4 2 5 8
```

Kết quả:

```text
-4 2 5 8
```

# Giải thích

- **Ví dụ 1:** Xóa $1, 4, 16$, còn lại $3, 7$.
- **Ví dụ 2:** $0, 1, 9, 25$ đều là số chính phương nên sau khi xóa còn `EMPTY`.
- **Ví dụ 3:** $-4 < 0$ không phải số chính phương nên tất cả phần tử được giữ nguyên.
