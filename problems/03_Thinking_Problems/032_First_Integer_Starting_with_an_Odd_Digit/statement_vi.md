# 032 - Bài 32: Giá trị đầu tiên có chữ số đầu là số lẻ

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tìm phần tử **đầu tiên** trong mảng có **chữ số đầu tiên** (chữ số có trọng số lớn nhất của $|a_i|$ ở hệ thập phân) là chữ số lẻ ($1, 3, 5, 7, 9$). Nếu không có phần tử nào thỏa mãn, in ra `0`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra giá trị đầu tiên thỏa mãn điều kiện, hoặc `0` nếu không tồn tại.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
24 68 -312 45 91
```

Kết quả:

```text
-312
```

# Ví dụ 2

Dữ liệu vào:

```text
4
0 21 48 802
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
3
1 20 30
```

Kết quả:

```text
1
```

# Giải thích

- **Ví dụ 1:** $24$ bắt đầu bằng $2$ (chẵn), $68$ bắt đầu bằng $6$ (chẵn), $-312$ có $|a_2| = 312$ bắt đầu bằng $3$ (lẻ).
- **Ví dụ 2:** Tất cả đều bắt đầu bằng chữ số chẵn ($0, 2, 4, 8$) nên in `0`.
- **Ví dụ 3:** $1$ bắt đầu bằng chữ số $1$ (lẻ).
