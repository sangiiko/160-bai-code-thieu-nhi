# 156 - Bài 156: Đổi chỗ giá trị lớn nhất và nhỏ nhất

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Gọi $mn = \min(a)$ là giá trị nhỏ nhất và $mx = \max(a)$ là giá trị lớn nhất của mảng. Hãy biến đổi mảng bằng cách thay mọi phần tử bằng $mx$ thành $mn$, và mọi phần tử bằng $mn$ thành $mx$ (các phần tử khác giữ nguyên).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra mảng sau khi biến đổi gồm $n$ số thực cách nhau bởi dấu cách (sai số $\le 10^{-6}$).

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
1.0 5.0 3.0 5.0 1.0
```

Kết quả:

```text
5.000000 1.000000 3.000000 1.000000 5.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
2.5 2.5 2.5 2.5
```

Kết quả:

```text
2.500000 2.500000 2.500000 2.500000
```

# Ví dụ 3

Dữ liệu vào:

```text
3
-5.0 0.0 10.0
```

Kết quả:

```text
10.000000 0.000000 -5.000000
```

# Giải thích

- **Ví dụ 1:** $mn = 1.0$ và $mx = 5.0$ được thay thế cho nhau ở mọi vị trí xuất hiện; $3.0$ giữ nguyên.
- **Ví dụ 2:** Vì $mn = mx = 2.5$ nên mảng không thay đổi.
- **Ví dụ 3:** $-5.0$ và $10.0$ đổi giá trị cho nhau.
