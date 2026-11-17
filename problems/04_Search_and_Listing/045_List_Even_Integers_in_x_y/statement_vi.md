# 045 - Bài 45: Liệt kê các số chẵn thuộc đoạn [x, y]

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$ và hai số nguyên $x, y$ ($x \le y$). Hãy liệt kê tất cả các **số chẵn** trong mảng thuộc đoạn $[x, y]$ theo đúng thứ tự xuất hiện.

# Dữ liệu vào

- Dòng đầu tiên chứa ba số nguyên $n, x, y$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các số chẵn thuộc $[x, y]$ cách nhau bởi dấu cách, hoặc `EMPTY` nếu không có.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le x \le y \le 10^9$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6 2 10
1 2 5 8 10 12
```

Kết quả:

```text
2 8 10
```

# Ví dụ 2

Dữ liệu vào:

```text
4 1 5
1 3 5 8
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
5 -4 4
-4 -3 0 2 5
```

Kết quả:

```text
-4 0 2
```

# Giải thích

- **Ví dụ 1:** Các số trong đoạn $[2, 10]$ là $2, 5, 8, 10$; trong đó các số chẵn là $2, 8, 10$.
- **Ví dụ 2:** Trong $[1, 5]$ chỉ có các số lẻ $1, 3, 5$ nên in `EMPTY`.
- **Ví dụ 3:** Các số chẵn thuộc $[-4, 4]$ là $-4, 0, 2$.
