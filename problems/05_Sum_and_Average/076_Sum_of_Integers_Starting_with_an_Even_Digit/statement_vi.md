# 076 - Bài 76: Tổng các số có chữ số đầu là chẵn

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tính tổng tất cả các phần tử có **chữ số đầu tiên** (chữ số đầu của $|a_i|$) là chữ số chẵn ($0, 2, 4, 6, 8$).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra tổng cần tìm dưới dạng số nguyên 64-bit.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
21 15 -42 60 33
```

Kết quả:

```text
39
```

# Ví dụ 2

Dữ liệu vào:

```text
4
11 35 71 99
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
3
0 800 -200
```

Kết quả:

```text
600
```

# Giải thích

- **Ví dụ 1:** $21, -42, 60$ bắt đầu bằng chữ số chẵn ($2, 4, 6$). Tổng $= 21 + (-42) + 60 = 39$.
- **Ví dụ 2:** Mọi số đều bắt đầu bằng chữ số lẻ; tổng bằng $0$.
- **Ví dụ 3:** $0, 800, -200$ bắt đầu bằng $0, 8, 2$; tổng $= 600$.
