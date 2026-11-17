# 133 - Bài 133: Tạo mảng b gồm 0, 1 thể hiện tính chẵn lẻ

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tạo mảng $b$ gồm $n$ phần tử chỉ nhận hai giá trị `0` hoặc `1` thể hiện tính chẵn lẻ của mảng $a$: đặt $b_i = 0$ nếu $a_i$ là số chẵn, và $b_i = 1$ nếu $a_i$ là số lẻ.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra $n$ số nguyên $b_0, b_1, \dots, b_{n-1}$ cách nhau bởi dấu cách.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
2 7 -4 9 0
```

Kết quả:

```text
0 1 0 1 0
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-1 -3 -5 1
```

Kết quả:

```text
1 1 1 1
```

# Ví dụ 3

Dữ liệu vào:

```text
3
0 2 4
```

Kết quả:

```text
0 0 0
```

# Giải thích

- **Ví dụ 1:** $2, -4, 0$ là số chẵn (`0`); $7, 9$ là số lẻ (`1`).
- **Ví dụ 2:** Số âm lẻ như $-1, -3, -5$ cũng cho giá trị `1` (cẩn thận toán tử `%` với số âm trong C/C++: `-3 % 2 == -1 != 0`).
- **Ví dụ 3:** Cả ba số đều chẵn nên mảng $b$ toàn `0`.
