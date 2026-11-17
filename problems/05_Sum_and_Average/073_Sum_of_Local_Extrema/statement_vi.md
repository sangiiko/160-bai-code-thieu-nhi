# 073 - Bài 73: Tổng các phần tử cực trị

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$ ($n \ge 2$). Một phần tử $a_i$ được gọi là **cực trị** nếu nó lớn hơn hẳn tất cả các phần tử xung quanh nó, **hoặc** nhỏ hơn hẳn tất cả các phần tử xung quanh nó. Hãy tính tổng tất cả các phần tử cực trị trong mảng.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra tổng các phần tử cực trị (sai số $\le 10^{-6}$).

# Giới hạn

- $2 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
4
1.0 5.0 2.0 6.0
```

Kết quả:

```text
14.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
5
1.0 3.0 2.0 2.0 5.0
```

Kết quả:

```text
9.000000
```

# Ví dụ 3

Dữ liệu vào:

```text
3
4.0 4.0 4.0
```

Kết quả:

```text
0.000000
```

# Giải thích

- **Ví dụ 1:** $1.0$ (cực tiểu), $5.0$ (cực đại), $2.0$ (cực tiểu), $6.0$ (cực đại) đều là cực trị; tổng $= 14.0$.
- **Ví dụ 2:** Chỉ có $1.0, 3.0, 5.0$ là cực trị ($2.0$ bằng với phần tử kề bên nên không phải cực trị); tổng $= 9.0$.
- **Ví dụ 3:** Không có cực trị nào nên tổng bằng $0$.
