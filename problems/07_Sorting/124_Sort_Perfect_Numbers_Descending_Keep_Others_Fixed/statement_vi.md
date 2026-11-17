# 124 - Bài 124: Sắp xếp số hoàn thiện giảm dần, giữ nguyên vị trí khác

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy sắp xếp tất cả các **số hoàn thiện** trong mảng theo thứ tự **giảm dần** trên các vị trí ban đầu của chúng, trong khi các phần tử không phải số hoàn thiện giữ nguyên vị trí.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra mảng kết quả gồm $n$ số nguyên cách nhau bởi dấu cách.

# Giới hạn

- $1 \le n \le 10^4$
- $-10^6 \le a_i \le 10^6$

# Ví dụ 1

Dữ liệu vào:

```text
5
6 10 28 5 496
```

Kết quả:

```text
496 10 28 5 6
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1 2 3 4
```

Kết quả:

```text
1 2 3 4
```

# Ví dụ 3

Dữ liệu vào:

```text
4
28 8128 12 6
```

Kết quả:

```text
8128 28 12 6
```

# Giải thích

- **Ví dụ 1:** Các số hoàn thiện $[6, 28, 496]$ tại chỉ số $0, 2, 4$ được sắp xếp giảm dần thành $[496, 28, 6]$; $10$ và $5$ giữ nguyên.
- **Ví dụ 2:** Không có số hoàn thiện nào nên mảng giữ nguyên.
- **Ví dụ 3:** Các số hoàn thiện $[28, 8128, 6]$ được sắp xếp giảm dần thành $[8128, 28, 6]$.
