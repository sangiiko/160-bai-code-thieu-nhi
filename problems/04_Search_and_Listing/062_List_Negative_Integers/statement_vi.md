# 062 - Bài 62: Liệt kê các số âm trong mảng số nguyên

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy liệt kê tất cả các phần tử mang giá trị **âm** ($a_i < 0$) theo đúng thứ tự xuất hiện trong mảng.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các số âm cách nhau bởi dấu cách, hoặc `EMPTY` nếu mảng không có số âm.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
-3 0 4 -10 2
```

Kết quả:

```text
-3 -10
```

# Ví dụ 2

Dữ liệu vào:

```text
4
0 1 2 100
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
3
-1 -2 -3
```

Kết quả:

```text
-1 -2 -3
```

# Giải thích

- **Ví dụ 1:** Các số âm là $-3$ và $-10$ ($0$ không phải số âm).
- **Ví dụ 2:** Không có phần tử âm nào nên in `EMPTY`.
- **Ví dụ 3:** Tất cả phần tử đều âm.
