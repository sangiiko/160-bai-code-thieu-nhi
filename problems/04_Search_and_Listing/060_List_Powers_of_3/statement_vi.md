# 060 - Bài 60: Liệt kê các giá trị có dạng 3^k

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy liệt kê tất cả các phần tử có dạng $3^k$ với $k$ là số nguyên không âm ($k \ge 0$, tức là $\{1, 3, 9, 27, \dots\}$) theo thứ tự xuất hiện. Nếu mảng không có giá trị nào dạng $3^k$, in ra `0`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các phần tử dạng $3^k$ cách nhau bởi dấu cách, hoặc `0` nếu không tồn tại.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
6 9 12 27 1
```

Kết quả:

```text
9 27 1
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-3 0 6 15
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
3
3 81 243
```

Kết quả:

```text
3 81 243
```

# Giải thích

- **Ví dụ 1:** $9 = 3^2$, $27 = 3^3$, $1 = 3^0$ đều có dạng $3^k$.
- **Ví dụ 2:** Không có phần tử nào là lũy thừa của $3$ nên in `0`.
- **Ví dụ 3:** Cả ba số $3^1, 3^4, 3^5$ đều hợp lệ.
