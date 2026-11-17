# 079 - Bài 79: Trung bình cộng các giá trị lớn hơn x

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$ và một số thực $x$. Hãy tính trung bình cộng của tất cả các phần tử **lớn hơn hẳn** $x$ ($a_i > x$). Nếu không có phần tử nào thỏa mãn, in ra `0`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$ và số thực $x$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra trung bình cộng cần tìm (sai số $\le 10^{-6}$).

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le x, a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5 4.0
1.0 5.0 4.0 7.0 9.0
```

Kết quả:

```text
7.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
4 10.0
1.0 5.0 10.0 -2.0
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
3 0.0
1.5 2.5 5.0
```

Kết quả:

```text
3.000000
```

# Giải thích

- **Ví dụ 1:** Các phần tử $> 4.0$ là $5.0, 7.0, 9.0$ ($4.0$ không lớn hơn hẳn); trung bình $= 21.0 / 3 = 7.0$.
- **Ví dụ 2:** Không có phần tử nào lớn hơn hẳn $10.0$; kết quả là $0$.
- **Ví dụ 3:** Trung bình $= (1.5 + 2.5 + 5.0) / 3 = 3.0$.
