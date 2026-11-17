# 059 - Bài 59: Liệt kê số nguyên có chữ số đầu là chẵn

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy liệt kê tất cả các phần tử có **chữ số đầu tiên** (chữ số đầu của $|a_i|$ ở hệ thập phân) là chữ số chẵn ($0, 2, 4, 6, 8$) theo thứ tự xuất hiện.

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
25 13 402 -67 99
```

Kết quả:

```text
25 402 -67
```

# Ví dụ 2

Dữ liệu vào:

```text
4
11 35 79 -90
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
3
0 81 200
```

Kết quả:

```text
0 81 200
```

# Giải thích

- **Ví dụ 1:** $25$ (đầu $2$), $402$ (đầu $4$), $-67$ (đầu $6$) có chữ số đầu chẵn.
- **Ví dụ 2:** Mọi phần tử bắt đầu bằng chữ số lẻ nên in `EMPTY`.
- **Ví dụ 3:** $0, 81, 200$ đều bắt đầu bằng chữ số chẵn.
