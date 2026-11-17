# 123 - Bài 123: Sắp xếp số nguyên tố tăng dần, giữ nguyên vị trí khác

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy sắp xếp tất cả các **số nguyên tố** trong mảng theo thứ tự tăng dần trên các vị trí ban đầu của chúng, trong khi các phần tử không phải số nguyên tố giữ nguyên vị trí.

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
6
7 4 2 9 5 1
```

Kết quả:

```text
2 4 5 9 7 1
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1 4 6 9
```

Kết quả:

```text
1 4 6 9
```

# Ví dụ 3

Dữ liệu vào:

```text
4
11 3 17 2
```

Kết quả:

```text
2 3 11 17
```

# Giải thích

- **Ví dụ 1:** Các số nguyên tố $[7, 2, 5]$ tại chỉ số $0, 2, 4$ được sắp xếp thành $[2, 5, 7]$; các số $4, 9, 1$ giữ nguyên.
- **Ví dụ 2:** Không có số nguyên tố nào nên mảng không thay đổi.
- **Ví dụ 3:** Cả $4$ số đều nguyên tố nên toàn bộ mảng được sắp xếp tăng dần.
