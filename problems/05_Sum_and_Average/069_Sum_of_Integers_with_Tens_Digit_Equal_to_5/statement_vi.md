# 069 - Bài 69: Tổng các số có chữ số hàng chục là 5

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tính tổng tất cả các phần tử có **chữ số hàng chục** (trong biểu diễn thập phân của $|a_i|$) bằng $5$, tức là $(\lfloor |a_i| / 10 \rfloor) \bmod 10 = 5$. Nếu không có phần tử nào thỏa mãn, kết quả là `0`.

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
52 158 45 -50 105
```

Kết quả:

```text
160
```

# Ví dụ 2

Dữ liệu vào:

```text
4
5 15 25 100
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
3
50 59 255
```

Kết quả:

```text
364
```

# Giải thích

- **Ví dụ 1:** $52, 158, -50$ có chữ số hàng chục là $5$. Tổng $= 52 + 158 - 50 = 160$.
- **Ví dụ 2:** $5$ không có chữ số hàng chục (bằng $0$); $15, 25, 100$ cũng không có hàng chục bằng $5$; kết quả là $0$.
- **Ví dụ 3:** Cả ba số $50, 59, 255$ đều có chữ số hàng chục là $5$; tổng bằng $364$.
