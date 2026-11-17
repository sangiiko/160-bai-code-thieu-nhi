# 056 - Bài 56: Liệt kê số nguyên có chữ số đầu là lẻ

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy liệt kê tất cả các phần tử trong mảng có **chữ số đầu tiên** (chữ số đầu của $|a_i|$ ở hệ thập phân) là chữ số lẻ ($1, 3, 5, 7, 9$) theo thứ tự xuất hiện.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các phần tử thỏa mãn cách nhau bởi dấu cách, hoặc `EMPTY` nếu không có.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
12 24 -35 48 91
```

Kết quả:

```text
12 -35 91
```

# Ví dụ 2

Dữ liệu vào:

```text
4
0 22 405 -81
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
3
1 30 500
```

Kết quả:

```text
1 30 500
```

# Giải thích

- **Ví dụ 1:** $12$ (đầu $1$), $-35$ (đầu $3$), $91$ (đầu $9$) đều có chữ số đầu lẻ.
- **Ví dụ 2:** Tất cả bắt đầu bằng chữ số chẵn ($0, 2, 4, 8$) nên in `EMPTY`.
- **Ví dụ 3:** Cả ba số đều bắt đầu bằng chữ số lẻ.
