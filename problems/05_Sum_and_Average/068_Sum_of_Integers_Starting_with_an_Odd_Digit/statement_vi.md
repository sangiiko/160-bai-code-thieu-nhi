# 068 - Bài 68: Tổng các số có chữ số đầu là lẻ

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tính tổng tất cả các phần tử trong mảng có **chữ số đầu tiên** (chữ số đầu của $|a_i|$) là chữ số lẻ. Nếu không có phần tử nào thỏa mãn, kết quả là `0`.

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
12 24 -35 41 7
```

Kết quả:

```text
-16
```

# Ví dụ 2

Dữ liệu vào:

```text
4
0 22 48 60
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
3
1000000000 300000000 500000000
```

Kết quả:

```text
1800000000
```

# Giải thích

- **Ví dụ 1:** Các số có chữ số đầu lẻ là $12, -35, 7$. Tổng $= 12 + (-35) + 7 = -16$.
- **Ví dụ 2:** Không có phần tử nào bắt đầu bằng chữ số lẻ nên tổng bằng $0$.
- **Ví dụ 3:** Cả ba số bắt đầu bằng $1, 3, 5$; tổng bằng $1.8 \times 10^9$.
