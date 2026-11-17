# 025 - Bài 25: Tìm đoạn [-x, x] chứa tất cả phần tử

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy tìm giá trị $x \ge 0$ nhỏ nhất sao cho đoạn đối xứng $[-x, x]$ chứa toàn bộ các phần tử trong mảng (tức $-x \le a_i \le x$ với mọi $i$).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số thực $x$ nhỏ nhất thỏa mãn (sai số tuyệt đối hoặc tương đối không quá $10^{-6}$).

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
-12.5 3.0 9.8 0.0 -4.2
```

Kết quả:

```text
12.500000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1.0 2.0 5.5 3.0
```

Kết quả:

```text
5.500000
```

# Ví dụ 3

Dữ liệu vào:

```text
3
0.0 0.0 0.0
```

Kết quả:

```text
0.000000
```

# Giải thích

- **Ví dụ 1:** Cần $x = \max |a_i| = \max(12.5, 9.8) = 12.5$ để đoạn $[-12.5, 12.5]$ bao phủ hết mảng.
- **Ví dụ 2:** Giá trị tuyệt đối lớn nhất là $5.5$, nên đoạn $[-5.5, 5.5]$ chứa hết mảng.
- **Ví dụ 3:** Mọi phần tử bằng $0$ nên $x = 0$.
